import React, { useState, useEffect } from 'react'
import Header from "../components/Header"
import S from '../style/Profile.module.css'
import Game_card from "../components/Game_card"
import FavouriteItem from "../components/FavouriteItem"
import Logo from '../img/Atomic Heart/LOGO.jpeg'
import { NavLink } from 'react-router-dom'

const Profile = () => {
  const [isEditing, setIsEditing] = useState(false)
  const [data, setData] = useState({
    username: localStorage.getItem('userName') || 'jerrytraitor',
    name: 'Jerry',
    email: 'jerry@gmail.com',
    telegram: '@jerryrat',
  })

  const handleButtonClick = () => {
    if (isEditing) alert('Данные успешно сохранены!')
    setIsEditing(prev => !prev)
  }

  const handleChange = (field, value) => {
    setData(prev => ({ ...prev, [field]: value }))
  }


  const context = require.context('../img/', true, /LOGO\.jpeg$/)
  const imageMap = {}
  context.keys().forEach((path) => {
      const folderName = path.split('/')[1]
      imageMap[folderName] = context(path)
  })


  const [games, setGames] = useState([])
  const [loading, setLoading] = useState(true)
  useEffect(() => {
    const fetchFavorites = async () => {
      try {

        const response = await fetch('http://127.0.0.1:8000/api/games/list')
        const data = await response.json()
        
        const finalData = data.results || data
        setGames(finalData.slice(0, 8))
        setLoading(false)
      } catch (error) {
        console.error('Ошибка:', error)
        setLoading(false)
      }
    }
    fetchFavorites()
  }, [])


return (
    <div className={S.wrapper}>
      <Header />
      <div className={S.container}>
        
        <div className={S.content} style={{ marginBottom: '40px', minHeight: 'auto' }}>
          <div className={S.container_info}>
            
            <div className={S.avatar_section}>
              <div className={S.avatar_wrapper}>
                <div className={S.profile_icon}>👤</div>
              </div>
              <button className={S.change_avatar_btn}>Изменить фото</button>
            </div>
            
            <div className={S.data_section}>
              <div className={S.column_left}>
                <div className={S.data_item}>
                  {isEditing ? (
                    <><label>Ник:</label>
                    <input type="text" name="username" value={data.username} onChange={(e) => handleChange('username', e.target.value)} className={S.input}/></>
                  ) : (
                    <h4>Ник: {data.username}</h4>
                  )}
                </div>
                <div className={S.data_item}>
                  {isEditing ? (
                    <><label>Имя:</label>
                    <input type="text" name="name" value={data.name} onChange={(e) => handleChange('name', e.target.value)} className={S.input}/></>
                  ) : (
                    <h4>Имя: {data.name}</h4>
                  )}
                </div>
              </div>

              <div className={S.column_right}>
                <div className={S.data_item}>
                  {isEditing ? (
                    <><label>Почта:</label>
                    <input type="email" name="email" value={data.email} onChange={(e) => handleChange('email', e.target.value)} className={S.input}/></>
                  ) : (
                    <h4>Почта: {data.email}</h4>
                  )}
                </div>
                <div className={S.data_item}>
                  {isEditing ? (
                    <><label>Telegram:</label>
                    <input type="text" name="telegram" value={data.telegram} onChange={(e) => handleChange('telegram', e.target.value)} className={S.input}/></>
                  ) : (
                    <h4>Telegram: {data.telegram}</h4>
                  )}
                </div>
                <button className={S.btn_edit} onClick={handleButtonClick}>
                  {isEditing ? 'Сохранить' : 'Изменить данные'}
                </button>
              </div>
            </div>

          </div>
        </div>
        <div className={S.content}>
          <h2 className={S.heading}>Избранное</h2>
            <div className={S.favorite_list}>
              {loading ? (
                <div style={{color: '#fff'}}>Загрузка списка...</div>
            ) : (
                games.map((game) => (
                    <FavouriteItem 
                        key={game.id} 
                        game={game} 
                        logo={imageMap[game.name] || Logo} 
                    />
                ))
            )}
            </div>
        </div>

      </div>
    </div>
  );
};

export default Profile;
