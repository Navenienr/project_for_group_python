import React, { useState, useRef, useEffect } from 'react';
import S from '../style/Header.module.css'
import { NavLink } from 'react-router-dom'

export const Header = () => {
    const [isOpen, setIsOpen] = useState(false);
    const menuRef = useRef(null);

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (menuRef.current && !menuRef.current.contains(event.target)) {
                setIsOpen(false);
            }
        };
        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, []);

     return (
        <header className={S.header}>
            <div className={S.nav_container}>
                <NavLink to="/" className={S.logo}>
                    <span className={S.logo_icon}>🎮</span>
                    GameForum
                </NavLink>

                <div className={S.header_search}>
                    <input type="text" className={S.hero_search_input} placeholder="Поиск..." />
                </div>

                <div className={S.header_actions}>
                    {/* кнопка телеграм */}
                    <a href="https://t.me/game_news_bot_1_bot" target="_blank" rel="noreferrer" className={S.tg_button}>
                        <svg 
                            width="20" 
                            height="20" 
                            viewBox="0 0 24 24" 
                            fill="none" 
                            xmlns="http://www.w3.org"
                            className={S.tg_icon_svg}
                        >
                            <path 
                                d="M22 2L2 10.5L9 13.5M22 2L15 22L9 13.5M22 2L9 13.5" 
                                stroke="white" 
                                strokeWidth="2" 
                                strokeLinecap="round" 
                                strokeLinejoin="round"
                            />
                            <path 
                                d="M9 13.5V19L12 16" 
                                stroke="white" 
                                strokeWidth="2" 
                                strokeLinecap="round" 
                                strokeLinejoin="round"
                            />
                        </svg>
                        <span className={S.tg_text}>Бот</span>
                    </a>

                    <div className={S.profile_wrapper} ref={menuRef}>
                        <div className={S.profile_section} onClick={() => setIsOpen(!isOpen)}>
                            <div className={S.profile_icon}>👤</div>
                            <div className={S.profile_name}>jerry</div>
                        </div>

                        {isOpen && (
                            <div className={S.popup_menu}>
                                <ul className={S.menu_list}>
                                    <li className={S.menu_item}>
                                        <NavLink to='/profile' className={S.navlink} onClick={() => setIsOpen(false)}>
                                            Профиль
                                        </NavLink>
                                    </li>
                                    <li className={S.menu_item}>
                                        <NavLink to='/login' className={S.navlink} onClick={() => setIsOpen(false)}>
                                            Выйти
                                        </NavLink>
                                    </li>
                                </ul>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </header>
    );
};

export default Header