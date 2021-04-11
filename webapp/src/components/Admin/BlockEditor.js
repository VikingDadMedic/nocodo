import { ControlType } from "property-controls";

import componentsList from "components/list";
import useAdmin from "services/stores/admin";
import Select from "components/Form/Select";
import { useEffect, useState } from "react";
import shallow from "zustand/shallow";

const Controls = ({ propertyControls, formData }) => {
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
          />
        </div>
      );
    }
  }

  return controls;
};

const BlockEditor = () => {
  const [formData, setFormData] = useState({});
  const { currentBlockType, currentPropertyControlValues } = useAdmin(
    (state) => ({
      currentBlockType: state.currentBlockType,
      currentPropertyControlValues: state.currentPropertyControlValues,
    }),
    shallow
  );

  useEffect(() => {
    setFormData(currentPropertyControlValues);
  }, [currentPropertyControlValues]);

  if (!!currentBlockType) {
    const componentItem = componentsList.find(
      (x) => x.name === currentBlockType.name
    );

    return (
      <>
        <h3 className="font-semibold text-xl leading-normal">
          Block: &lt;{currentBlockType.name} /&gt;
        </h3>

        <Controls
          propertyControls={componentItem.propertyControls}
          formData={formData}
        />
      </>
    );
  } else {
    return <p>You have not selected any block to edit</p>;
  }
};

export default BlockEditor;
