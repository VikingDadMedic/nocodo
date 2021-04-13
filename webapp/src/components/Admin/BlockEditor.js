import { ControlType } from "property-controls";

import componentsList from "components/list";
import useAdmin from "services/stores/admin";
import Select from "components/Form/Select";
import { useEffect, useState } from "react";
import shallow from "zustand/shallow";
import { classBasedStyleControls } from "./classBasedStyleControls";

const Controls = ({
  propertyControls,
  formData,
  onChange,
  allowedClassBasedStyleControls = undefined,
}) => {
  const controls = [];
  let allControls = {
    ...propertyControls,
  };
  if (!!allowedClassBasedStyleControls) {
    allControls = {
      ...allControls,
      ...allowedClassBasedStyleControls.map((x) =>
        x in classBasedStyleControls ? classBasedStyleControls[x] : undefined
      ),
    };
  }

  for (const x of Object.keys(allControls)) {
    const definition = allControls[x];
    if (definition["type"] === ControlType.Enum) {
      const options = definition["options"].reduce(
        (acc, item, i) => [
          ...acc,
          {
            label:
              "optionTitles" in definition
                ? definition["optionTitles"][i]
                : item,
            value: item,
          },
        ],
        []
      );

      const getValue = (row) => row.value;
      const getLabel = (row) => row.label;

      controls.push(
        <div key={`ctrl-${x}`} className="inline-block mx-4">
          <Select
            label={x}
            name={x}
            options={options}
            formData={formData}
            getLabel={getLabel}
            getValue={getValue}
            onChange={onChange}
          />
        </div>
      );
    }
  }

  return controls;
};

const BlockEditor = () => {
  const [formData, setFormData] = useState({});
  const {
    currentBlockType,
    currentPropertyControlValues,
    setPropertyControlValue,
  } = useAdmin(
    (state) => ({
      currentBlockType: state.currentBlockType,
      currentPropertyControlValues: state.currentPropertyControlValues,
      setPropertyControlValue: state.setPropertyControlValue,
    }),
    shallow
  );

  useEffect(() => {
    setFormData(currentPropertyControlValues);
  }, [currentPropertyControlValues]);

  if (!currentBlockType) {
    return <p>You have not selected any block to edit</p>;
  }

  const handleChange = (name, value) => {
    setFormData((state) => ({
      ...state,
      [name]: value,
    }));

    setPropertyControlValue(name, value);
  };

  const componentItem = componentsList.find((x) => x.name === currentBlockType);

  return (
    <>
      <h6 className="mb-2 text-xs uppercase font-semibold text-gray-500">
        Block: &lt;{currentBlockType} /&gt;
      </h6>

      <div className="flex">
        <Controls
          allowedClassBasedStyleControls={
            componentItem.allowedClassBasedStyleControls
          }
          propertyControls={componentItem.propertyControls}
          formData={formData}
          onChange={handleChange}
        />
      </div>
    </>
  );
};

export default BlockEditor;
