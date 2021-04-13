import loadable from "@loadable/component";
import { ControlType } from "property-controls";

const componentsList = [
  {
    name: "Button",
    help:
      "Use a Button to get user's confirmation, cancellation or other action.",
    component: loadable(() => import("components/Form/Button")),
    allowedClassBasedStyleControls: [
      "fontSize",
      "color",
      "textAlign",
      "backgroundColor",
    ],
    propertyControls: {},
  },
  {
    name: "Text",
    help: "A Text block can format and display text from CMS or user input.",
    component: loadable(() => import("components/Content/Text")),
    allowedClassBasedStyleControls: ["fontSize", "color", "textAlign"],
    propertyControls: {
      tag: {
        type: ControlType.Enum,
        options: ["h1", "h2", "h3", "h4", "h5", "h6", "p"],
        optionTitles: [
          "Heading 1",
          "Heading 2",
          "Heading 3",
          "Heading 4",
          "Heading 5",
          "Heading 6",
          "Paragraph",
        ],
      },
    },
  },
  {
    name: "Hero",
    component: loadable(() => import("components/Content/Hero")),
    propertyControls: {
      intro: {
        type: ControlType.ComponentInstance,
        allowedComponents: ["Text"],
        defaultProps: [
          {
            tag: "p",
            fontSize: "base",
            className: "uppercase tracking-loose w-full",
            children: "What business are you?",
          },
        ],
      },
      title: {
        type: ControlType.ComponentInstance,
        allowedComponents: ["Text"],
        defaultProps: [
          {
            tag: "h1",
            fontSize: "5xl",
            className: "my-4 font-bold leading-tight",
            children: "Main Hero Message to sell yourself!",
          },
        ],
      },
      subTitle: {
        type: ControlType.ComponentInstance,
        allowedComponents: ["Text"],
        defaultProps: [
          {
            tag: "p",
            fontSize: "2xl",
            className: "leading-normal mb-8",
            children:
              "Sub-hero message, not too long and not too short. Make it just right!",
          },
        ],
      },
      cta: {
        type: ControlType.ComponentInstance,
        allowedComponents: ["Button"],
        defaultProps: [
          {
            backgroundColor: "white",
            className:
              "mx-auto lg:mx-0 hover:underline text-gray-800 font-bold rounded-full my-6 py-4 px-8 shadow-lg focus:outline-none focus:shadow-outline transform transition hover:scale-105 duration-300 ease-in-out",
            children: "Register!",
          },
        ],
      },
    },
  },
  {
    name: "Hero3",
    component: loadable(() => import("components/Content/Hero3")),
    propertyControls: {},
  },
];

export default componentsList;
