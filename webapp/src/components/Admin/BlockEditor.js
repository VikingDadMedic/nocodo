import { ControlType } from "property-controls";

import componentsList from "components/list";
import useAdmin from "services/stores/admin";
import Select from "components/Form/Select";
import { useEffect, useState } from "react";
import shallow from "zustand/shallow";

const Controls = ({ propertyControls, formData, onChange }) => {
  const controls = [];

  for (const x of Object.keys(propertyControls)) {
    const definition = propertyControls[x];
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
        <div key={`ctrl-${x}`} className="my-6">
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
      <h3 className="font-semibold text-xl leading-normal">
        Block: &lt;{currentBlockType} /&gt;
      </h3>

      <Controls
        propertyControls={componentItem.propertyControls}
        formData={formData}
        onChange={handleChange}
      />
    </>
  );
};

export default BlockEditor;
