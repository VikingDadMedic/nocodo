import create from "zustand";

const initialState = {
  isInWidgetAdmin: false,
  currentWidget: null,
};

const useAdmin = create((set, get) => ({
  ...initialState,

  toggleEditing: (value = undefined) => {
    set((state) => ({
      ...state,
      isInWidgetAdmin: value !== undefined ? value : !state.isInWidgetAdmin,
    }));
  },

  setCurrentWidget: (widgetState) => {
    set((state) => ({
      ...state,
      currentWidget: widgetState,
    }));
  },
}));

export default useAdmin;
