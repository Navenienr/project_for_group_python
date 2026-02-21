import React from 'react'
import S from '../style/Main.module.css'

const Sidebar = () => {
  return (
    <aside className={S.sidebar}>
        <div className={S.sidebar_scroll_container}>
            {/* Разделы меню */}
            <div className={S.sidebar_section}>
                <h3 className={S.sidebar_title}>Меню</h3>
                <ul className={S.sidebar_menu}>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                </ul>
            </div>

            <div className={S.sidebar_section}>
                <h3 className={S.sidebar_title}>Разделы</h3>
                <ul className={S.sidebar_menu}>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                </ul>
            </div>

            <div className={S.sidebar_section}>
                <h3 className={S.sidebar_title}>Категории</h3>
                <ul className={S.sidebar_menu}>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                </ul>
            </div>

            <div className={S.sidebar_section}>
                <h3 className={S.sidebar_title}>Дополнительно</h3>
                <ul className={S.sidebar_menu}>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                    <li><a href="#">Пункт меню</a></li>
                </ul>
            </div>

        </div>
    </aside>
  )
}

export default Sidebar