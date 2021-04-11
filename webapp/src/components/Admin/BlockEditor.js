import { ControlType } from "property-controls";

import componentsList from "components/list";
import useAdmin from "services/stores/admin";
import Select from "components/Form/Select";
import { useState } from "react";

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
  const currentWidget = useAdmin((state) => state.currentWidget);
  const componentItem = componentsList.find(
    (x) => x.name === currentWidget.name
  );
  const Component = componentItem.component;

  return (
    <>
      <span className="text-xs">{currentWidget.uuid}</span>

      <Controls
        propertyControls={componentItem.propertyControls}
        formData={formData}
      />
    </>
  );
};

export default BlockEditor;
