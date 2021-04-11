import { createElement } from "react";

const Text = ({
  tag = "p",
  className = undefined,
  size = undefined,
  color = undefined,
  align = undefined,
  text = undefined,
  isInBlockAdmin = false,
  onClick = undefined,
  children,
}) => {
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
  if (isInBlockAdmin) {
    innerClassName = `${innerClassName} hover:outline-blue cursor-default`;
  }
  const innerChildren = children || text;

  const handleClick = () => {
    if (!!onClick) {
      onClick();
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
