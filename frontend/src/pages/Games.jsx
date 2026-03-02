import React, { useState, useRef, useEffect } from 'react'
import Header from "../components/Header"
import S from '../style/Games.module.css'
import Sidebar from '../components/Sidebar'
import Game_card from '../components/Game_card'
import Logo from '../img/Atomic Heart/LOGO.jpeg'
import { NavLink } from 'react-router-dom'

const Games = () => {
  const context = require.context('../img/', true, /LOGO\.jpeg$/)
  const limit = 16

  const gamesList = context.keys().map((path, index) => {
    const imagePath = context(path)
    const folderName = path.split('/')[1];

    return {
      id: index,
      folder: folderName,
      title: folderName.replace(/-/g, ' '), 
      image: imagePath
    }
  })

  return (
    <div>
        <Header/>
        <div className={S.main_container}>
            <Sidebar/>
            <div className={S.content}>
                <div className={S.game_content}>
                    {gamesList.slice(0, limit).map((game) => (
                      <NavLink 
                        key={game.id} 
                        to={`/game/${game.folder}`} 
                        style={{ textDecoration: 'none' }}
                      >
                        <Game_card image={game.image} title={game.title} />
                      </NavLink>
                    ))}
                </div>
            </div>
        </div>
    </div>
  )
}

export default Games