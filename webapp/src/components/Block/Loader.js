import { ControlType } from "property-controls";

import componentsList from "components/list";

const BlockLoader = ({ name, defaultProps = {} }) => {
  const componentItem = componentsList.find((x) => x.name === name);
  const Component = componentItem.component;
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
  return (
    <>
      <Component {...props} />
    </>
  );
};

export default BlockLoader;
