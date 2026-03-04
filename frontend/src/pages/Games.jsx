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

  const [currentPage, setCurrentPage] = useState(1)
  const [totalPages, setTotalPages] = useState(0)
  const [hasNext, setHasNext] = useState(false)   
  const [hasPrev, setHasPrev] = useState(false) 




  useEffect(() => {
    const get_games = async (page) => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/games/shortlist/?page=${page}`)
        const data = await response.json();
        
        setGames(data.results)
        setHasNext(!!data.next)
        setHasPrev(!!data.previous)
        // вычисление количества страниц 
        setTotalPages(Math.ceil(data.count / 16)) 
        await new Promise(resolve => setTimeout(resolve, 300))
        setLoading(false)
      } catch (error) {
        console.error('Ошибка:', error)
        setLoading(false)
      }
    }
    get_games(currentPage)
  }, [currentPage])

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
                    {loading ? <SkeletonLoader type="card" count={12} /> : renderedGames}
                </div>
                <div className={S.pagination}>
                  <button onClick={() => setCurrentPage(prev => prev - 1)} disabled={!hasPrev}className={S.page_btn}>
                      ❮ Назад
                  </button>
                  
                  <span className={S.page_info}>Страница {currentPage} из {totalPages}</span>

                  <button onClick={() => setCurrentPage(prev => prev + 1)} disabled={!hasNext}className={S.page_btn}>
                      Вперед ❯
                  </button>
              </div>
            </div>
        </div>
    </div>
 )
}

export default Games;