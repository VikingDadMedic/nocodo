import HeroImage from "assets/images/hero.png";
import useAdmin from "services/stores/admin";

export const Hero = ({
  title,
  intro = undefined,
  subTitle = undefined,
  cta = undefined,
  onClick = undefined,
}) => {
  const isInBlockAdmin = useAdmin((state) => state.isInBlockAdmin);

  const handleClick = !!onClick ? onClick : undefined;

  return (
    <div
      className={`pt-24 ${isInBlockAdmin ? "hover:outline-blue" : ""}`}
      onClick={handleClick}
    >
      <div className="container px-3 mx-auto flex flex-wrap flex-col md:flex-row items-center">
        <div className="flex flex-col w-full md:w-2/5 justify-center items-start text-center md:text-left">
          {!!intro ? <>{intro}</> : null}

          {title}

          {!!subTitle ? <>{subTitle}</> : null}

          {!!cta ? <>{cta}</> : null}
        </div>

        <div className="w-full md:w-3/5 py-6 text-center">
          <img className="w-full md:w-4/5 z-50" src={HeroImage} alt="Hero" />
        </div>
      </div>
    </div>
  );
};

export default Hero;
