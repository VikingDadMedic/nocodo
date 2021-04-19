import { useHistory } from "react-router-dom";

const Button = ({
  name,
  className = undefined,
  icon = undefined,
  isDisabled = false,
  linkTo = undefined,
  onClick = undefined,
  children,
}) => {
  const history = useHistory();
  let innerClassName = `bg-white px-2 rounded-sm ${className}`;

  if (icon !== undefined) {
    if (children === undefined) {
      children = <img src={icon} alt="Button" />;
    } else {
      children = (
        <>
          <img src={icon} alt="Button" className="float-left mr-1" />
          {children}
        </>
      );
    }
  }

  let handleClick = undefined;
  if (isDisabled) {
    handleClick = undefined;
  } else if (!!onClick) {
    handleClick = () => {
      onClick(name);
    };
  } else if (!!linkTo) {
    handleClick = () => {
      history.push(linkTo);
    };
  }

  return (
    <button className={innerClassName} onClick={handleClick}>
      {children}
    </button>
  );
};

export default Button;
