import { useState } from "react";

import Label from "./Label";

const Inner = ({ options, getValue, getLabel }) => {
  return (
    <select>
      {options.map((x) => (
        <option key={`opt-${getValue(x)}`} value={getValue(x)}>
          {getLabel(x)}
        </option>
      ))}
    </select>
  );
};

const Select = (props) => {
  const {
    name,
    options,
    formData,
    formError,
    getValue,
    getLabel,
    label = undefined,
    isRequired = false,
    onChange = undefined,
  } = props;
  const [filteredOptions, setFilteredOptions] = useState(options);

  const ErrorComponent = () => {
    if (!!formError && name in formError) {
      return (
        <div className="text-sm text-red-600 px-4 py-1">{formError[name]}</div>
      );
    }
    return null;
  };

  let inner = null;

  if (!!label) {
    inner = (
      <div>
        <div>
          <Label isRequired={isRequired} name={name}>
            {label}
          </Label>
        </div>

        <Inner {...props} />

        <ErrorComponent />
      </div>
    );
  } else {
    inner = (
      <>
        <Inner {...props} />
        <ErrorComponent />
      </>
    );
  }

  return inner;
};

export default Select;
