import create from "zustand";

const initialState = {
  isInBlockAdmin: false,
  currentBlockType: null,
  currentBlockId: null,
  currentPropertyControlValues: {},
};

const useAdmin = create((set, get) => ({
  ...initialState,

  toggleEditing: (value = undefined) => {
    set((state) => ({
      ...state,
      isInBlockAdmin: value !== undefined ? value : !state.isInBlockAdmin,
      currentBlockType:
        value === false || (value === undefined && state.isInBlockAdmin)
          ? null
          : state.currentBlockType,
      currentPropertyControlValues:
        value === false || (value === undefined && state.isInBlockAdmin)
          ? {}
          : state.currentPropertyControlValues,
    }));
  },

  setCurrentBlock: (blockType, blockId, propertyControlValues = {}) => {
    set((state) => ({
      ...state,
      currentBlockType: blockType,
      currentBlockId: blockId,
      currentPropertyControlValues: {
        ...propertyControlValues,
      },
    }));
  },

  setPropertyControlValues: (mapping) => {
    set((state) => ({
      ...state,
      currentPropertyControlValues: {
        ...mapping,
      },
    }));
  },

  setPropertyControlValue: (name, value) => {
    set((state) => ({
      ...state,
      currentPropertyControlValues: {
        ...state.currentPropertyControlValues,
        [name]: value,
      },
    }));
  },
}));

export default useAdmin;
