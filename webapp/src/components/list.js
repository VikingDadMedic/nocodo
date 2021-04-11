import loadable from "@loadable/component";
import { ControlType } from "property-controls";

const componentsList = [
  // {
  //   name: "Button",
  //   help:
  //     "Use a Button to get user's confirmation, cancellation or other action.",
  //   component: Loadable({
  //     loader: () => import("components/Form/Button"),
  //   }),
  // },
  // {
  //   name: "Text input",
  //   help: "Use a text input to let user share information like name, age, etc.",
  //   component: Loadable({
  //     loader: () => import("components/Form/Input")
  //   }),
  // },
  // {
  //   name: "Large text",
  //   help:
  //     "Use a large text (textarea) to let user share paragraphs of text easily.",
  //   component: loadable(() => import("components/Form/Textarea")),
  // },
  // {
  //   name: "Checkbox",
  //   help:
  //     "Use checkbox(es) to let user to select one or more of multiple options.",
  //   component: loadable(() => import("components/Form/Checkbox")),
  // },
  // {
  //   name: "Radio",
  //   help: "Use radio(s) to let user select only one of multiple options.",
  //   component: loadable(() => import("components/Form/Radio")),
  // },
  // {
  //   name: "Options (dropdown, pills)",
  //   help: "Use radio(s) to let user select only one of multiple options.",
  //   component: loadable(() => import("components/Form/Radio")),
  // },
  {
    name: "Text",
    component: loadable(() => import("components/Content/Text")),
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
      size: {
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
      align: {
        type: ControlType.Enum,
        options: ["left", "center", "right", "justify"],
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
            className: "my-4 font-bold leading-tight",
            size: "5xl",
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
            className: "leading-normal mb-8",
            size: "2xl",
            children:
              "Sub-hero message, not too long and not too short. Make it just right!",
          },
        ],
      },
    },
  },
];

export default componentsList;
