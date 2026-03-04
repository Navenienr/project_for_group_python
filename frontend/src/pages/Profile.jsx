import React, { useState } from 'react'
import Header from "../components/Header"
import S from '../style/Profile.module.css'
import Game_card from "../components/Game_card"
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

  // Логика картинок
  const context = require.context('../img/', true, /LOGO\.jpeg$/)
  const gamesList = context.keys().map((path, index) => {
    const imagePath = context(path)
    const folderName = path.split('/')[1] 
    return {
      id: index,
      folder: folderName,
      title: folderName.replace(/-/g, ' '), 
      image: imagePath
    }
  })


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
          <div className={S.game_content}>
            {gamesList.slice(0, 16).map((game) => (
              <NavLink key={game.id} to={`/game/${game.folder}`} style={{ textDecoration: 'none' }}>
                <Game_card image={game.image} title={game.title} />
              </NavLink>
            ))}
          </div>
        </div>

      </div>
    </div>
  );
};

export default Profile;
