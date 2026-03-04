import React, { useState } from 'react'
import S from '../style/Post.module.css'

const Post = ({ data }) => {
  
  const [isLiked, setIsLiked] = useState (false)
  const date = new Date(data.published_at);
  const formattedDate = date.toLocaleDateString('ru-RU'); 
  const formattedTime = date.toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' })

  if (!data) return null;
  return (
    <div className={S.news_post}>
        <div className={S.post_main}>
            <div className={S.post_header}>
                <div className={S.post_author}>
                    <div className={S.author_avatar}>👤</div>
                    <div className={S.author_info}>
                        <div className={S.author_name}>{data.author_name}</div>
                        <div className={S.post_time}>{formattedDate} в {formattedTime}</div>
                    </div>
                </div>
            </div>

            <div className={S.post_body}>
                <h3 className={S.post_title}>{data.title}</h3>
                <p className={S.post_excerpt}>{data.short_description}</p>
                <div className={S.post_image_content}>[Изображение]</div>
            </div>

            <div className={S.post_stats}>
                <button 
                    className={`${S.stat_item} ${isLiked ? S.liked : ''}`} 
                    onClick={() => setIsLiked(!isLiked)}
                >
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                    </svg>
                    <span>{data.likes_count}</span>
                </button>
                
                <div className={S.stat_item}>
                    <span>💬 {data.comments_count}</span>
                </div>
                
                <div className={S.stat_item}>
                    <span>👁️ {data.views_count}</span>
                </div>
            </div>
        </div>

        <div className={S.post_comments_sidebar}>
            <h4 className={S.comments_title}>Комментарии</h4>
            <div className={S.comments_list}>
                <div className={S.comment_item}>
                    <span className={S.comment_user}>User1:</span> комментарий 1
                </div>
                <div className={S.comment_item}>
                    <span className={S.comment_user}>User2:</span> комментарий 2
                </div>
            </div>
            <div className={S.comment_input_wrapper}>
                <input type="text" placeholder="Написать..." className={S.comment_input} />
            </div>
        </div>
    </div>
  )
}

export default Post
