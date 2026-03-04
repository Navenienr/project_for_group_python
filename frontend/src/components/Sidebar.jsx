import React from 'react'
import S from '../style/Sidebar.module.css'
import { NavLink } from 'react-router-dom'

const Sidebar = () => {
  return (
    <aside className={S.sidebar}>
        <div className={S.sidebar_scroll_container}>
            <div className={S.sidebar_section}>
                <NavLink to='/games' className={S.sidebar_title}>Игры</NavLink>
                <ul className={S.sidebar_menu}>
                    <li><a href="#">RPG</a></li>
                    <li><a href="#">Шутеры</a></li>
                    <li><a href="#">Симуляторы</a></li>
                    <li><a href="#">Головоломки</a></li>
                    <li><a href="#">Рогалики</a></li>
                    <li><a href="#">Стратегии</a></li>
                    <li><a href="#">Ещё</a></li>
                </ul>
            </div>

            <div className={S.sidebar_section}>
                <h3 className={S.sidebar_title}>Статьи</h3>
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