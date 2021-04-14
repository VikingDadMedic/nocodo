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

  return createElement(
    tag,
    {
      className,
      onClick,
    },
    innerChildren
  );
};

export default Text;
