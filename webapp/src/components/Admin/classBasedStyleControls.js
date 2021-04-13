import { ControlType } from "property-controls";

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
};
