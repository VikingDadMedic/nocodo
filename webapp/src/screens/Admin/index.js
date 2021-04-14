// import TopNavigation from "components/Navigation/TopNavigation";
import { useEffect } from "react";

import useAdmin from "services/stores/admin";
import BlockEditor from "components/Block/Editor";
import BlockLoader from "components/Block/Loader";

const EditorBar = () => {
  const blockId = useAdmin((state) => state.blockId);

  return (
    <div className="fixed z-50 top-0 left-0 h-24 w-full bg-gray-200 border-l-2 border-gray-300 p-2">
      {!!blockId ? (
        <BlockEditor />
      ) : (
        <h6 className="mb-2 text-xs uppercase font-semibold text-gray-500">
          Click on a Block to edit
        </h6>
      )}
    </div>
  );
};

const Admin = () => {
  const toggleEditing = useAdmin((state) => state.toggleEditing);

  useEffect(() => {
    toggleEditing(true);

    return () => {
      toggleEditing(false);
    };
  }, [toggleEditing]);

  return (
    <>
      {/* <TopNavigation /> */}
      <div className="mt-14" />

      {/* <h1>Welcome to nocodo Admin</h1> */}

      <EditorBar />

      <BlockLoader blockType="Hero" />
    </>
  );
};

export default Admin;
