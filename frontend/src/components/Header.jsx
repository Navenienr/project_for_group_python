import React, { useState, useRef, useEffect } from 'react';
import S from '../style/Main.module.css'
import H from '../style/Header.module.css'
import {Link, NavLink} from 'react-router-dom'

export const Header = () => {

    const [isOpen, setIsOpen] = useState(false);
    const menuRef = useRef(null);

    // закрытие меню при клике вне его
    useEffect(() => {
        const handleClickOutside = (event) => {
        if (menuRef.current && !menuRef.current.contains(event.target)) {
            setIsOpen(false);
        }
        };
        document.addEventListener('mousedown', handleClickOutside);
        return () => {
        document.removeEventListener('mousedown', handleClickOutside);
        };
    }, []);

  return (
    <header className={S.header}>
            <div className={S.nav_container}>
                <NavLink to="/ " className={S.logo}>
                    <span className={S.logo_icon}>🎮</span>
                    GameForum
                </NavLink>

                <div className={S.header_search}>
                    <input type="text" className={S.hero_search_input} placeholder="Поиск..." />
                </div>

                <div className={S.profile_section}  onClick={() => setIsOpen(!isOpen)} >
                    <div className={S.profile_icon}>👤</div>
                    <div className={S.profile_name}>jerry</div>
                </div>
                      {isOpen && (
                        <div className={H.popup_menu} ref={menuRef} >
                        <ul className={H.menu_list}>
                            <li className={H.menu_item}>
                            <NavLink to='/profile' 
                                className={H.navlink}
                                onClick={() => {
                                setIsOpen(false);
                                }}>Профиль
                            </NavLink>
                            </li>
                            <li className={H.menu_item}>
                            <NavLink to='/login'
                                className={H.navlink}
                                onClick={() => {
                                setIsOpen(false);
                                }}
                            >
                                Выйти
                            </NavLink>
                            </li>
                        </ul>
                        </div>
                    )}

            </div>
        </header>
  )
}
export default Header