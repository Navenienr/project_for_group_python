import React, { useState, useEffect } from 'react'
import S from '../style/Main.module.css'
import Post from './Post'
import Sidebar from './Sidebar'
import Header from './Header'
import SkeletonLoader from './SkeletonLoader'
import { useLocation } from 'react-router-dom'

export default function Main() {
  const [news, setNews] = useState([])
  const [loading, setLoading] = useState(true)
  const location = useLocation () // хук для отслеживания изменений в URL (сортировки)

  useEffect(() => {
    const get_news_and_comments = async () => {
      try {
        setLoading(true)

        // извлекаем параметр ordering из URL (?ordering=-likes_count_attr)
        const queryParams = new URLSearchParams(location.search)
        const ordering = queryParams.get('ordering') || '-published_at' // по умолчанию новые

        let token = localStorage.getItem('userToken')
        if (token) {
            token = token.replace(/"/g, '').trim()
        }

        const requestHeaders = {
          'Content-Type': 'application/json'
        }

        if (token) {
          requestHeaders['Authorization'] = `Bearer ${token}`
        }

        const response = await fetch(`http://127.0.0.1:8000/api/news/news/?ordering=${ordering}`, {
          method: 'GET',
          headers: requestHeaders
        })

        const data = await response.json()
        const newsData = data.results || data
        setNews(newsData)

        // искусственная задержка для скелетона
        await new Promise(resolve => setTimeout(resolve, 800))
        setLoading(false)

      } catch (error) {
        console.error('Ошибка при загрузке новостей:', error)
        setLoading(false)
      }
    }

    get_news_and_comments()
  }, [location.search]) 

  const queryParams = new URLSearchParams(location.search)
  const ordering = queryParams.get('ordering')

  let subTitle = "новые"

  if (ordering === "-likes_count_attr") {
      subTitle = "популярные"
  } else if (ordering === "-published_at") {
      subTitle = "новые"
  }
 
  return (
    <div>
        <Header/>
        <div className={S.main_container}>
            <Sidebar/>
            <div className={S.content}>
                <h2 className={S.section_title}>Статьи <span className={S.subtitle}>/ {subTitle}</span></h2>
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
