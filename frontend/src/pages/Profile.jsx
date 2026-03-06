import React, { useState, useEffect } from 'react'
import Header from "../components/Header"
import S from '../style/Profile.module.css'
import FavouriteItem from "../components/FavouriteItem"
import Logo from '../img/Atomic Heart/LOGO.jpeg'

const Profile = () => {
  const [isEditing, setIsEditing] = useState(false);
  const [loading, setLoading] = useState(true);
  const [games, setGames] = useState([])
  
  const [data, setData] = useState({
    username: '',
    name: '',
    email: '',
    telegram: '',
  });

  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem('userToken')?.replace(/"/g, '').trim();
      
      try {
        const response = await fetch('http://127.0.0.1:8000/api/core/profile/', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        
        if (response.ok) {
          const profileData = await response.json();
          setData({
            username: profileData.username,
            name: profileData.first_name || 'Не указано',
            email: profileData.email,
            telegram: profileData.telegram_chat_id || '@не_привязан', 
          });
        }
      } catch (error) {
        console.error('Ошибка загрузки профиля:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, []);

  // загрузка логотипов
  const context = require.context('../img/', true, /LOGO\.jpeg$/)
  const imageMap = {}
  context.keys().forEach((path) => {
      const folderName = path.split('/')[1]
      imageMap[folderName] = context(path)
  })

  // загрузка списка избранного
  useEffect(() => {
    const fetchFavorites = async () => {
      const token = localStorage.getItem('userToken')?.replace(/"/g, '').trim();
      try {
        const response = await fetch('http://127.0.0.1:8000/api/games/favorites/', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        const result = await response.json();
        const finalData = result.results || result;
        setGames(finalData);
      } catch (error) {
        console.error('Ошибка загрузки избранного:', error);
      } finally {
        setLoading(false);
      }
    }
    fetchFavorites();
  }, []);

  // функция удаления из избранного
  const handleRemove = async (gameId) => {
    const token = localStorage.getItem('userToken')?.replace(/"/g, '').trim();
    const url = `http://127.0.0.1:8000/api/games/${gameId}/favorite/remove/`;
    
    try {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: { 
                'Authorization': `Bearer ${token}` 
            }
        });

        if (response.ok) {
            // фильтрация по айди игры внутри объекта избранного
            setGames(prev => prev.filter(item => {
                const idInItem = item.game_details?.id || item.game || item.id;
                return idInItem !== gameId;
            }));
        } else {
            alert("Не удалось удалить из избранного");
        }
    } catch (error) {
        console.error("Ошибка при удалении:", error);
    }
  };

  const handleButtonClick = () => {
    if (isEditing) alert('Данные успешно сохранены!')
    setIsEditing(prev => !prev)
  }

  const handleChange = (field, value) => {
    setData(prev => ({ ...prev, [field]: value }))
  }

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
                    <input type="text" value={data.username} onChange={(e) => handleChange('username', e.target.value)} className={S.input}/></>
                  ) : (
                    <h4>Ник: {data.username}</h4>
                  )}
                </div>
                <div className={S.data_item}>
                  {isEditing ? (
                    <><label>Имя:</label>
                    <input type="text" value={data.name} onChange={(e) => handleChange('name', e.target.value)} className={S.input}/></>
                  ) : (
                    <h4>Имя: {data.name}</h4>
                  )}
                </div>
              </div>

              <div className={S.column_right}>
                <div className={S.data_item}>
                  {isEditing ? (
                    <><label>Почта:</label>
                    <input type="email" value={data.email} onChange={(e) => handleChange('email', e.target.value)} className={S.input}/></>
                  ) : (
                    <h4>Почта: {data.email}</h4>
                  )}
                </div>
                <div className={S.data_item}>
                  {isEditing ? (
                    <><label>Telegram:</label>
                    <input type="text" value={data.telegram} onChange={(e) => handleChange('telegram', e.target.value)} className={S.input}/></>
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
            ) : games.length > 0 ? (
              games.map((item) => {
                // извлекаем данные игры
                const gameData = item.game_details || item;
                return (
                  <FavouriteItem 
                    key={item.id} 
                    game={gameData} 
                    logo={imageMap[gameData.name] || Logo} 
                    onRemove={() => handleRemove(gameData.id)} 
                  />
                )
              })
            ) : (
              <div style={{color: '#ccc', padding: '20px'}}>Список избранного пуст</div>
            )}
          </div>
        </div>

      </div>
    </div>
  );
};

export default Profile;