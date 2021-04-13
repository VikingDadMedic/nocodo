import { createElement } from "react";

const Text = ({
  tag = "p",
  className = undefined,
  text = undefined,
  onClick = undefined,
  children,
}) => {
  if (!children && !text && (children === "" || text === "")) {
    return null;
  }
  const innerChildren = children || text;

  const handleClick = !!onClick ? onClick : undefined;

  return createElement(
    tag,
    {
      className,
      onClick: handleClick,
    },
    innerChildren
  );
};

export default Text;
