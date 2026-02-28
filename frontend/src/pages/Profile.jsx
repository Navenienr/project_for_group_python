import React, { useState, useRef, useEffect } from 'react';
import Header from "../components/Header";
import M from "..//style/Main.module.css";
import S from '..//style/Profile.module.css';
import Game_card from "../components/Game_card";
import { NavLink } from 'react-router-dom'


const Profile = () => {
  const [isEditing, setIsEditing] = useState(false)

  const handleButtonClick = () => {
    if (isEditing) {
      alert('Данные сохранены!')
    }
    setIsEditing(prev => !prev)
  }

  const [data, setData] = useState({
    username: 'jerrytraitor',
    name: 'Jerry',
    email: 'jerry@gmail.com',
    telegram: '@jerryrat',
    birthDate: '01.01.1111',
  });

  const handleChange = (field, value) => {
    setData(prev => ({ ...prev, [field]: value }));
  }

  const context = require.context('../img/', true, /LOGO\.jpeg$/);
  const limit = 16;

  const gamesList = context.keys().map((path, index) => {
    const imagePath = context(path);
    const folderName = path.split('/')[1]; 

    return {
      id: index,
      folder: folderName,
      title: folderName.replace(/-/g, ' '), 
      image: imagePath
    };
  });


  return (
    <div className={S.wrapper}>
      <Header></Header>
      <div className={S.container}>
        
        <div className={S.container_info}>
          <div className={S.avatar_section}>
            <div className={S.avatar_wrapper}>
              <div className={S.profile_icon}>👤</div>
            </div>
          <button className={S.change_avatar_btn}>Изменить</button>
          </div>
          
          {isEditing ? (
             <div className={S.data_section}>
                <div className={S.column_left}>
                    <div className={S.data_item}>
                      <input type="text" value={data.nik} onChange={(e) => handleChange('nik', e.target.value)} className={S.input}/>
                    </div>

                    <div className={S.data_item}>
                      <input type="text" value={data.name} onChange={(e) => handleChange('nik', e.target.value)} className={S.input}/>
                    </div>

                    <div className={S.data_item}>
                      <input type="email" value={data.email} onChange={(e) => handleChange('nik', e.target.value)} className={S.input}/>
                    </div>
                </div>

                <div className={S.column_right}>
                    <div className={S.data_item}>
                      <input type="text" value={data.telegram} onChange={(e) => handleChange('nik', e.target.value)} className={S.input}/>
                    </div>

                    <div className={S.data_item}>
                      <input type="date" value={data.birthDate} onChange={(e) => handleChange('nik', e.target.value)} className={S.input}/>
                    </div>

                    <button className={S.btn_edit} onClick={handleButtonClick}>Сохранить</button>

                </div>
                
             </div>

            ) : (
                <div className={S.data_section}>
                  <div className={S.column_left}>
                    <div className={S.data_item}>
                      <h4>Ник: {data.nik}</h4>
                    </div>

                    <div className={S.data_item}>
                        <h4>Имя: {data.name}</h4>
                    </div>

                    <div className={S.data_item}>
                      <h4>Почта: {data.email}</h4>
                    </div>
                  </div>

                  <div className={S.column_right}>
                    <div className={S.data_item}>
                      <h4>Telegram: {data.telegram}</h4>
                    </div>

                    <div className={S.data_item}>
                        <h4>Дата рождения: {data.birthDate}</h4>
                    </div>

                    <button className={S.btn_edit} onClick={handleButtonClick}>Изменить</button>
      
                  </div>
                </div>
        )}

      </div>
        

        <div className={S.content} >
          <h2 className={S.heading}>Избранное</h2>
            <div className={S.game_content}>
              {gamesList.slice(0, limit).map((game) => (
                      <NavLink 
                        key={game.id} 
                        to={`/game/${game.folder}`} 
                        style={{ textDecoration: 'none' }}
                      >
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



