import { createElement } from "react";

const Text = ({
  tag = "p",
  className = undefined,
  fontSize = undefined,
  color = undefined,
  align = undefined,
  text = undefined,
  isInBlockAdmin = false,
  isBlockSelected = false,
  onClick = undefined,
  children,
}) => {
  if (!children && !text && (children === "" || text === "")) {
    return null;
  }
  let innerClassName = className || "";
  if (!!fontSize) {
    innerClassName = `${innerClassName} text-${fontSize}`;
  }
  if (!!color) {
    innerClassName = `${innerClassName} text-${color}`;
  }
  if (isInBlockAdmin) {
    innerClassName = `${innerClassName} hover:outline-blue cursor-default`;
  }
  if (isBlockSelected) {
    innerClassName = `${innerClassName} outline-blue`;
  }
  const innerChildren = children || text;

  const handleClick = !!onClick ? onClick : undefined;

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
