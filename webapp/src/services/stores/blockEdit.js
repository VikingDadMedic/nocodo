import create from "zustand";

const useBlockEdit = create((set, get) => ({
  blocks: {},

  toggleEditing: () => {
    set({
      blocks: {},
    });
  },

  setEditingBlock: (blockId, blockType, propertyControlValues) => {
    set({
      blocks: {
        [blockId]: {
          blockType,
          propertyControlValues,
        },
      },
    });
  },

  setPropertyControlValue: (blockId, name, value) => {
    set((state) => ({
      ...state,

      blocks: {
        [blockId]: {
          ...state,
          propertyControlValues: {
            ...state[blockId],
            [name]: value,
          },
        },
      },
    }));
  },
}));

export default useBlockEdit;
