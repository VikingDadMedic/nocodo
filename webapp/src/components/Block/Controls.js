import { ControlType } from "property-controls";

import Select from "components/Form/Select";
import { classBasedStyleControls } from "./classBasedStyleControls";

const BlockControls = ({
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
      ...allowedClassBasedStyleControls.reduce(
        (acc, x) => ({
          ...acc,
          [x]:
            x in classBasedStyleControls
              ? classBasedStyleControls[x]
              : undefined,
        }),
        {}
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

export default BlockControls;
