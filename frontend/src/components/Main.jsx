import React, { useState, useEffect } from 'react'
import S from '../style/Main.module.css'
import Post from './Post'
import Sidebar from './Sidebar'
import Header from './Header'
import SkeletonLoader from './SkeletonLoader'

export default function Main() {
  const [news, setNews] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const get_news = async () => {
      try {
        let token = localStorage.getItem('userToken');
        if (token) {
            token = token.replace(/"/g, '').trim();
        }

        const requestHeaders = {
          'Content-Type': 'application/json'
        }

        if (token) {
          requestHeaders['Authorization'] = `Bearer ${token}`;
        }

        const response = await fetch('http://127.0.0.1:8000/api/news/news/', {
          method: 'GET',
          headers: requestHeaders
        })

        const data = await response.json();
        const newsData = data.results || data;
        setNews(newsData);
        await new Promise(resolve => setTimeout(resolve, 500));
        setLoading(false);

      } catch (error) {
        console.error('Ошибка:', error);
        setLoading(false);
      }
    };
    get_news();
  }, []);

  
  return (
    <div>
        <Header/>
        <div className={S.main_container}>
            <Sidebar/>
            <div className={S.content}>
                <h2 className={S.section_title}>Статьи</h2>
                <div className={S.posts_list}>
                    {loading ? (
                        <SkeletonLoader type="list" count={3} />
                    ) : news.length > 0 ? (
                        news.map((item) => (
                            <Post key={item.id} data={item} />
                        ))
                    ) : (
                        <p>Новостей пока нет...</p>
                    )}
                </div>
            </div>
        </div>
    </div>
  )
}
