import React, { useState } from 'react'
import Header from '../components/Header'
import Sidebar from '../components/Sidebar'
import S from '../style/Game.module.css'
import Card from '../img/baldursgate.jpg'
import { useParams } from 'react-router-dom'

const Game = () => {
    const { folderName } = useParams();
    
    const context = require.context('../img/', true, /\.(jpg|jpeg|png)$/);
    const allPaths = context.keys();

    let bgImg = Card
    const bgPath = allPaths.find(path => 
        path.includes(`./${folderName}/`) && path.includes('Заставка')
    );
    if (bgPath) bgImg = context(bgPath)


    let logoImg = Card;
    const logoPath = allPaths.find(path => 
        path.includes(`./${folderName}/`) && path.includes('LOGO')
    );
    if (logoPath) logoImg = context(logoPath)


    const screenshots = allPaths
        .filter(path => path.includes(`./${folderName}/`) && path.includes('gameplay'))
        .map(context);

    const displayScreens = screenshots.length > 0 ? screenshots : Array(5).fill(Card)

    const [activeIndex, setActiveIndex] = useState(0);

    const nextSlide = () => setActiveIndex((prev) => (prev === displayScreens.length - 1 ? 0 : prev + 1));
    const prevSlide = () => setActiveIndex((prev) => (prev === 0 ? displayScreens.length - 1 : prev - 1));
    console.log("Путь к фону:", bgImg)

    return (
        <div className={S.shader}>
            <div 
                className={S.bg_overlay} 
                style={{ backgroundImage: `url(${bgImg})` }}
            ></div>
            
            <Header />
            <div className={S.main_container}>
                <Sidebar />
                <div className={S.content}>
                    <div className={S.card_container}>
                        <div className={S.game_img}>
                            <div className={S.game_heading}>
                                <div className={S.logo} style={{ backgroundImage: `url(${logoImg})`, backgroundSize: 'cover' }}></div>
                                <div>
                                    <h2 style={{ margin: 0, fontSize: '1.2rem', color: '#fff' }}>
                                        {folderName ? folderName.replace(/-/g, ' ') : "Загрузка..."}
                                    </h2>
                                    <p style={{ margin: 0, fontSize: '0.8rem', opacity: 0.7, color: '#fff' }}>Категория игры</p>
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
                                        <p className={S.text_value}>v1.0.0.0</p>
                                    </div>
                                    <div className={S.info_row}>
                                        <h3 className={S.text_label}>Языки</h3>
                                        <p className={S.text_value}>Русский, Английский</p>
                                    </div>
                                    <div className={S.info_row}>
                                        <h3 className={S.text_label}>Разработчик</h3>
                                        <p className={S.text_value}>Неизвестен</p>
                                    </div>
                                    <div className={S.info_row}>
                                        <h3 className={S.text_label}>Устройства</h3>
                                        <p className={S.text_value}>PC, Steam Deck</p>
                                    </div>
                                    <div className={S.info_row}>
                                        <h3 className={S.text_label}>Архитектура</h3>
                                        <p className={S.text_value}>x64 (Windows)</p>
                                    </div>
                                </div>
                                <button className={S.btn_download}>Скачать</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};


export default Game;