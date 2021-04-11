import { ControlType } from "property-controls";
import shallow from "zustand/shallow";

import componentsList from "components/list";
import useAdmin from "services/stores/admin";

const BlockLoader = ({ name, defaultProps = {} }) => {
  const componentItem = componentsList.find((x) => x.name === name);
  const Component = componentItem.component;
  const {
    isInBlockAdmin,
    setCurrentBlock,
    setPropertyControlValues,
  } = useAdmin(
    (state) => ({
      isInBlockAdmin: state.isInBlockAdmin,
      setCurrentBlock: state.setCurrentBlock,
      setPropertyControlValues: state.setPropertyControlValues,
    }),
    shallow
  );

  const props = {
    ...defaultProps,
  };
  for (const x of Object.keys(componentItem.propertyControls)) {
    const definition = componentItem.propertyControls[x];
    if (definition["type"] === ControlType.ComponentInstance) {
      const innerComponent = definition["allowedComponents"][0];
      const innerDefaultProps = definition["defaultProps"][0];

      props[x] = (
        <BlockLoader name={innerComponent} defaultProps={innerDefaultProps} />
      );
    }
  }

  const handleClick = () => {
    if (isInBlockAdmin) {
      // We are in admin/CMS mode, we let the app know which block we are
      setCurrentBlock(
        {
          name,
        },
        props
      );
    }
  };

  return (
    <>
      <Component
        {...props}
        isInBlockAdmin={isInBlockAdmin}
        onClick={handleClick}
      />
    </>
  );
};

export default BlockLoader;
