import { ControlType } from "property-controls";

const colorOptionsAndLabels = () => {
  const colors = ["gray", "blue", "green"];
  const values = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900];
  const options = colors.reduce(
    (acc, color) => [...acc, ...values.map((v) => `${color}-${v}`)],
    []
  );

  return {
    options,
  };
};

export const classBasedStyleControls = {
  fontSize: {
    type: ControlType.Enum,
    options: [
      "xs",
      "sm",
      "base",
      "lg",
      "xl",
      "2xl",
      "3xl",
      "4xl",
      "5xl",
      "6xl",
      "7xl",
      "8xl",
      "9xl",
    ],
  },

  color: {
    type: ControlType.Enum,
    options: [],
  },

  textAlign: {
    type: ControlType.Enum,
    options: ["left", "center", "right", "justify"],
  },

  backgroundColor: {
    type: ControlType.Enum,
    options: [],
  },
};
