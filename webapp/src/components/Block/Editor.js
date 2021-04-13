import { useEffect, useState } from "react";
import shallow from "zustand/shallow";

import componentsList from "components/list";
import useAdmin from "services/stores/admin";
import BlockControls from "./Controls";

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
        <BlockControls
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
