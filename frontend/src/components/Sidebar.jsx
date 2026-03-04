import React from 'react'
import S from '../style/Sidebar.module.css'
import { NavLink } from 'react-router-dom'
import { useState, useEffect } from 'react'

const Sidebar = () => {
    const [genres, setGenres] = useState([])
    const [showAll, setShowAll] = useState(false);
    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/games/genres/')
            .then(res => res.json())
            .then(data => setGenres(data))
            .catch(err => console.error(err))
    }, [])

    const displayedGenres = showAll ? genres : genres.slice(0, 7)


  return (
    <aside className={S.sidebar}>
        <div className={S.sidebar_scroll_container}>
            <div className={S.sidebar_section}>
                <NavLink to='/games' className={S.sidebar_title}>Игры</NavLink>
                <ul className={S.sidebar_menu}>
                    {displayedGenres.map(genre => (
                        <li key={genre.id}>
                            <NavLink 
                                to={`/games?genre=${genre.id}`} 
                                className={({ isActive }) => isActive ? S.active : ''}
                            >
                                {genre.name}
                            </NavLink>
                        </li>
                    ))}
                    {genres.length > 7 && (
                        <li>
                            <button 
                                className={S.more_btn} 
                                onClick={() => setShowAll(!showAll)}
                            >
                                {showAll ? '❮ Скрыть' : 'Ещё...'}
                            </button>
                        </li>
                    )}
                    </ul>
            </div>

            <div className={S.sidebar_section}>
                <NavLink to='/' className={S.sidebar_title}>Статьи</NavLink>
                <ul className={S.sidebar_menu}>
                    <li><a href="#">Новые</a></li>
                    <li><a href="#">Популярные</a></li>
                </ul>
            </div>

            <div className={S.sidebar_section}>
                <h3 className={S.sidebar_title}>Программы</h3>
                <ul className={S.sidebar_menu}>
                    <li><a href="#">Windows</a></li>
                    <li><a href="#">MacOS</a></li>
                </ul>
            </div>

        </div>
    </aside>
  )
}

export default Sidebar