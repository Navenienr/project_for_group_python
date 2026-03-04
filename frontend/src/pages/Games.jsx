import React, { useState, useRef, useEffect, useLayoutEffect, useMemo } from 'react'
import Header from "../components/Header"
import S from '../style/Games.module.css'
import Sidebar from '../components/Sidebar'
import Game_card from '../components/Game_card'
import Logo from '../img/Atomic Heart/LOGO.jpeg'
import { NavLink } from 'react-router-dom'
import SkeletonLoader from '../components/SkeletonLoader'

const context = require.context('../img/', true, /LOGO\.jpeg$/)
const imageMap = {}

context.keys().forEach((path) => {
    const parts = path.split('/')
    const folderName = parts[1]
    imageMap[folderName] = context(path)
})

const Games = () => {
  const [games, setGames] = useState([])
  const [loading, setLoading] = useState(true)
  const limit = 16

  useEffect(() => {
    const get_games = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/games/shortlist/')
        const data = await response.json()
        
        const finalData = data.results || data
        await new Promise(resolve => setTimeout(resolve, 500))
        setGames(finalData)
        setLoading(false)
      } catch (error) {
        console.error('Ошибка:', error)
        setLoading(false)
      }
    }
    get_games()
  }, [])

  const renderedGames = useMemo(() => {
    return games.slice(0, limit).map((game) => (
      <NavLink 
        key={game.id} 
        to={`/game/${game.id}`} 
        style={{ textDecoration: 'none' }}
      >
        <Game_card 
          image={imageMap[game.name] || Logo} 
          title={game.name} 
        />
      </NavLink>
    ))
  }, [games]) 


 return (
    <div>
        <Header />
        <div className={S.main_container}>
            <Sidebar />
            <div className={S.content}>
                <div className={S.game_content}>
                    {loading ? (
                        Array(12).fill(0).map((item, index) => (
                            <div key={index} className={S.skeleton_item }>
                                <div className={S.skeleton_card}></div>
                                <div className={S.skeleton_title}></div>
                            </div>
                        ))
                    ) : (
                        renderedGames
                    )}
                </div>
            </div>
        </div>
    </div>
 )
}

export default Games;