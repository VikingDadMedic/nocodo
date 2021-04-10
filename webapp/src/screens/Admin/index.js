// import TopNavigation from "components/Navigation/TopNavigation";
import { useEffect } from "react";

import { HeroBlock } from "components/Page/Block";
import componentsList from "components/list";
import useAdmin from "services/stores/admin";

const WidgetControls = () => {
  const currentWidget = useAdmin((state) => state.currentWidget);
  const componentItem = componentsList.find(
    (x) => x.name === currentWidget.name
  );
  const Component = componentItem.component;

  return (
    <>
      <span className="text-xs">{currentWidget.uuid}</span>
      {/* <Component text="Text" /> */}

      <Component>Sample</Component>
    </>
  );
};

const Sidebar = () => {
  const currentWidget = useAdmin((state) => state.currentWidget);

  return (
    <div className="fixed z-50 top-0 right-0 h-screen w-64 bg-gray-200 border-l-2 border-gray-300 p-2">
      <h6 className="mb-2 text-xs uppercase font-semibold text-gray-500">
        Click on a Widget to edit
      </h6>

      {!!currentWidget && <WidgetControls />}
    </div>
  );
};

const Admin = () => {
  const toggleEditing = useAdmin((state) => state.toggleEditing);

  useEffect(() => {
    toggleEditing(true);
  }, [toggleEditing]);

  return (
    <>
      {/* <TopNavigation /> */}
      <div className="mt-14" />

      {/* <h1>Welcome to nocodo Admin</h1> */}

      <Sidebar />

      <HeroBlock />
    </>
  );
};

export default Admin;
