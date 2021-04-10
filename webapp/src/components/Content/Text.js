import { createElement } from "react";
import shallow from "zustand/shallow";

import useAdmin from "services/stores/admin";

const Text = ({
  tag = "p",
  className = undefined,
  size = undefined,
  color = undefined,
  text = undefined,
  align = undefined,
  children,
}) => {
  const { isInWidgetAdmin, setCurrentWidget } = useAdmin(
    (state) => ({
      isInWidgetAdmin: state.isInWidgetAdmin,
      setCurrentWidget: state.setCurrentWidget,
    }),
    shallow
  );

  if (!children && !text && (children === "" || text === "")) {
    return null;
  }
  let innerClassName = className || "";
  if (!!size) {
    innerClassName = `${innerClassName} text-${size}`;
  }
  if (!!color) {
    innerClassName = `${innerClassName} text-${color}`;
  }
  if (isInWidgetAdmin) {
    innerClassName = `${innerClassName} hover:outline-blue cursor-default`;
  }
  const innerChildren = children || text;

  const handleClick = () => {
    if (isInWidgetAdmin) {
      // We are in admin/CMS mode, we let the app know which element we are
      setCurrentWidget({
        name: "Text",
      });
    }
  };

  return createElement(
    tag,
    {
      className: innerClassName,
      onClick: handleClick,
    },
    innerChildren
  );
};

export default Text;
