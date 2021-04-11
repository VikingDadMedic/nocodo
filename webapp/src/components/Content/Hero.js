import HeroImage from "assets/images/hero.png";
import useAdmin from "services/stores/admin";

export const Hero = ({ title, intro = undefined, subTitle = undefined }) => {
  const isInWidgetAdmin = useAdmin((state) => state.isInWidgetAdmin);

  return (
    <div className={`pt-24 ${isInWidgetAdmin ? "hover:outline-blue" : ""}`}>
      <div className="container px-3 mx-auto flex flex-wrap flex-col md:flex-row items-center">
        <div className="flex flex-col w-full md:w-2/5 justify-center items-start text-center md:text-left">
          {!!intro ? <>{intro}</> : null}

          {title}

          {!!subTitle ? <>{subTitle}</> : null}

          <button className="mx-auto lg:mx-0 hover:underline bg-white text-gray-800 font-bold rounded-full my-6 py-4 px-8 shadow-lg focus:outline-none focus:shadow-outline transform transition hover:scale-105 duration-300 ease-in-out">
            Subscribe
          </button>
        </div>

        <div className="w-full md:w-3/5 py-6 text-center">
          <img className="w-full md:w-4/5 z-50" src={HeroImage} alt="Hero" />
        </div>
      </div>
    </div>
  );
};

export default Hero;
