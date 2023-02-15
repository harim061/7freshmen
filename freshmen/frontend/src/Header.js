import chatBalloon from "./img/chatBalloon.png";
import styled from "styled-components";
import COLOR from "./utils/color.js";

const Header = () => {
  return (
    <div className="header">
      <ImgBox>
        <img src={chatBalloon} alt="chatBalloon" />
      </ImgBox>
    </div>
  );
};

const ImgBox = styled.div`
  height: 139px;
  background: ${COLOR.yellow};
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  margin-top: 79px;
  padding-top: 8px;
  display: flex;
  justify-content: center;
  align-items: flex-end;
`;

export default Header;
