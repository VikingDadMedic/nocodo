import { useHistory } from "react-router-dom";

const Button = ({
  className = undefined,
  icon = undefined,
  isDisabled = false,
  linkTo = undefined,
  onClick = undefined,
  children,
}) => {
  const history = useHistory();

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
    handleClick = onClick;
  } else if (!!linkTo) {
    handleClick = () => {
      history.push(linkTo);
    };
  }

  return (
    <button className={className} onClick={handleClick}>
      {children}
    </button>
  );
};

export default Button;
