import React, { useState, useEffect } from 'react' 
import Header from '../components/Header'
import Sidebar from '../components/Sidebar'
import S from '../style/Game.module.css'
import Card from '../img/baldursgate.jpg'
import { useParams } from 'react-router-dom'
import SkeletonLoader from '../components/SkeletonLoader'

const Game = () => {
    const { id } = useParams() 
    const [game, setGame] = useState(null)
    const [activeIndex, setActiveIndex] = useState(0)
    const [isFavorite, setIsFavorite] = useState(false)

    useEffect(() => {
        const fetchGame = async () => {
          try {
            const response = await fetch(`http://127.0.0.1:8000/api/games/${id}`)
            const data = await response.json()
            await new Promise(resolve => setTimeout(resolve, 700))
            
            setGame(data)
          } catch (error) {
            console.error('Ошибка:', error)
          }
        }
        fetchGame()
    }, [id])
    const context = require.context('../img/', true, /\.(jpg|jpeg|png)$/)
    const allPaths = context.keys()

    let bgImg = Card
    let logoImg = Card
    let displayScreens = Array(5).fill(Card)

    if (game) {
        const folderName = game.name 

        const bgPath = allPaths.find(path => 
            path.includes(`./${folderName}/`) && path.includes('Заставка')
        )
        if (bgPath) bgImg = context(bgPath)

        const logoPath = allPaths.find(path => 
            path.includes(`./${folderName}/`) && path.includes('LOGO')
        )
        if (logoPath) logoImg = context(logoPath)

        const screenshots = allPaths
            .filter(path => path.includes(`./${folderName}/`) && path.includes('gameplay'))
            .map(context)
        
        if (screenshots.length > 0) displayScreens = screenshots
    }

    const nextSlide = () => setActiveIndex((prev) => (prev === displayScreens.length - 1 ? 0 : prev + 1))
    const prevSlide = () => setActiveIndex((prev) => (prev === 0 ? displayScreens.length - 1 : prev - 1))

    return (
        <div className={S.shader}>
            <div className={S.bg_overlay} style={{ backgroundImage: `url(${bgImg})` }}></div>
            <Header />
            <div className={S.main_container}>
                <Sidebar />
                <div className={S.content}>
                     {game ? (
                        <>
                            <div className={S.card_container}>
                                <div className={S.game_img}>
                                    <div className={S.game_heading}>
                                        <div className={S.logo} style={{ backgroundImage: `url(${logoImg})` }}></div>
                                        <div className={S.heading_text}>
                                            <h2>{game.name}</h2>
                                            <p>{game.genres.map(g => g.name).join(', ')}</p>
                                        </div>
                                    </div>

                                    <div className={S.carousel_container}>
                                        <div className={S.main_display}>
                                            <button className={S.arrow_left} onClick={prevSlide}>❮</button>
                                            <button className={S.arrow_right} onClick={nextSlide}>❯</button>
                                            <img className={S.main_img} src={displayScreens[activeIndex]} alt="Gameplay" />
                                        </div>
                                        <div className={S.thumbs_list}>
                                            {displayScreens.slice(0, 5).map((img, index) => (
                                                <div 
                                                    key={index} 
                                                    className={`${S.thumb_item} ${activeIndex === index ? S.active : ''}`}
                                                    onClick={() => setActiveIndex(index)}
                                                >
                                                    <img src={img} alt="Thumbnail" />
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                </div>

                                <div className={S.game_info_wrapper}>
                                    <div className={S.game_info}>
                                        <div className={S.text_container}> 
                                            <div className={S.info_row}>
                                                <h3 className={S.text_label}>Версия</h3>
                                                <p className={S.text_value}>{game.version}</p>
                                            </div>
                                            <div className={S.info_row}>
                                                <h3 className={S.text_label}>Языки</h3>
                                                <p className={S.text_value}>
                                                    {game.interface_language.map(l => l.name).join(', ')}
                                                </p>
                                            </div>
                                            <div className={S.info_row}>
                                                <h3 className={S.text_label}>Разработчик</h3>
                                                <p className={S.text_value}>{game.developer}</p>
                                            </div>
                                            <div className={S.info_row}>
                                                <h3 className={S.text_label}>Дата выхода</h3>
                                                <p className={S.text_value}>{game.release_date || 'Неизвестна'}</p>
                                            </div>
                                        </div>
                                        <div className={S.actions_container}>
                                            <a href={game.download_link} className={S.btn_download} target="_blank" rel="noreferrer">
                                                Скачать
                                            </a>
                                            <button 
                                                className={`${S.btn_favorite_text} ${isFavorite ? S.active : ''}`}
                                                onClick={() => setIsFavorite(!isFavorite)}
                                            >
                                                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org">
                                                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                                                </svg>
                                                {isFavorite ? 'Убрать из избранного' : 'В избранное'}
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div className={S.details_wrapper}>
                                <div className={S.description_section}>
                                    <h2 className={S.section_title}>Об игре</h2>
                                    <p className={S.description_text}>{game.description}</p>
                                </div>

                                <div className={S.requirements_section}>
                                    <h2 className={S.section_title}>Системные требования</h2>
                                    <div className={S.req_grid}>
                                        <div className={S.req_column}>
                                            <h3>Минимальные</h3>
                                            <p>{game.min_requirements}</p>
                                        </div>
                                        <div className={S.req_column}>
                                            <h3>Рекомендуемые</h3>
                                            <p>{game.rec_requirements}</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </>
                    ) : (
                        <SkeletonLoader type="details" />
                    )}
                </div>
            </div>
        </div>
    )
}

export default Game
