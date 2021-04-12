import { ControlType } from "property-controls";
import shallow from "zustand/shallow";

import componentsList from "components/list";
import useAdmin from "services/stores/admin";
import { useEffect, useState } from "react";

let unsavedId = 2147483647;

const BlockLoader = ({
  blockType,
  id = undefined,
  defaultProps = {},
  savedProps,
}) => {
  const componentItem = componentsList.find((x) => x.name === blockType);
  const Component = componentItem.component;
  const {
    isInBlockAdmin,
    setCurrentBlock,
    currentBlockId,
    currentPropertyControlValues,
  } = useAdmin(
    (state) => ({
      isInBlockAdmin: state.isInBlockAdmin,
      setCurrentBlock: state.setCurrentBlock,
      currentBlockId: state.currentBlockId,
      currentPropertyControlValues: state.currentPropertyControlValues,
    }),
    shallow
  );

  const [blockId] = useState(!!id ? id : ++unsavedId);
  const [props, setProps] = useState({
    ...defaultProps,
  });

  useEffect(() => {
    if (blockId === currentBlockId) {
      setProps((state) => ({
        ...state,
        ...currentPropertyControlValues,
      }));
    }
  }, [currentPropertyControlValues, currentBlockId]);

  for (const x of Object.keys(componentItem.propertyControls)) {
    const definition = componentItem.propertyControls[x];
    if (definition["type"] === ControlType.ComponentInstance) {
      const innerComponent = definition["allowedComponents"][0];
      const innerDefaultProps = definition["defaultProps"][0];

      props[x] = (
        <BlockLoader
          blockType={innerComponent}
          defaultProps={innerDefaultProps}
        />
      );
    }
  }

  const handleClick = (event) => {
    event.stopPropagation();
    if (isInBlockAdmin) {
      // We are in admin/CMS mode, we let the app know which block we are
      setCurrentBlock(blockType, blockId, props);
    }
  };

  return (
    <>
      <Component
        {...props}
        isInBlockAdmin={isInBlockAdmin}
        isBlockSelected={blockId === currentBlockId}
        onClick={handleClick}
      />
    </>
  );
};

export default BlockLoader;
