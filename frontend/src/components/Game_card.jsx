import React from 'react'
import S from '..//style/Game_card.module.css'
import { NavLink } from 'react-router-dom'


const Game_card = ({ image, title }) => {
  return (
    <div className={S.cover_container}>
      <div className={S.cover_content}>
        <img className={S.game_image} src={image} alt={title} />
      </div>
      <h3>{title}</h3>
    </div>
  );
};

export default Game_card