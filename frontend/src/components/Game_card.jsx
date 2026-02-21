import React from 'react'
import S from '..//style/Game_card.module.css';

const Game_card = () => {
  return (
    <div className={S.cover_container}>
        <div className={S.cover_content}>
        <div className={S.icon_placeholder}>🎮</div>
        </div>
    </div>
  )
}

export default Game_card