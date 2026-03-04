import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import S from '../style/FavouriteItem.module.css';

const Favourites = ({ game, logo }) => {
    const [isFavorite, setIsFavorite] = useState(true);

    if (!isFavorite) return null;

    return (
        <div className={S.favorite_row}>
            <NavLink to={`/game/${game.id}`} className={S.game_link}>
                <div className={S.logo} style={{ backgroundImage: `url(${logo})` }}></div>
                <div className={S.heading_text}>
                    <h2>{game.name}</h2>
                    <p>{game.genres?.map(g => g.name).join(', ') || 'Жанры не указаны'}</p>
                </div>
            </NavLink>

            <div className={S.favorite_wrapper}>
                <button 
                    className={`${S.favorite_btn} ${S.active}`}
                    onClick={() => setIsFavorite(false)}
                    title="Убрать из избранного"
                >
                    <div className={S.heart_container}>
                        <svg className={S.heart_left} viewBox="0 0 24 24" xmlns="http://www.w3.org">
                            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09V21.35z" />
                        </svg>
                        <svg className={S.heart_right} viewBox="0 0 24 24" xmlns="http://www.w3.org">
                            <path d="M12 21.35V5.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                        </svg>
                    </div>
                </button>
            </div>
        </div>
    );
};

export default Favourites;
