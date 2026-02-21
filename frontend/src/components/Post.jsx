import React from 'react'
import S from '../style/Main.module.css'


const Post = () => {
  return (
    <div className={S.news_post}>
        <div className={S.post_header}>
            <div className={S.post_author}>
                <div className={S.author_avatar}>👤</div>
                <div className={S.author_info}>
                    <div className={S.author_name}>Имя автора</div>
                    <div className={S.post_time}>17:45</div>
                </div>
            </div>
            <div className={S.post_category}>Категория</div>
        </div>

        <div className={S.post_content}>
            <h3 className={S.post_title}>Заголовок поста</h3>
            <p className={S.post_excerpt}>Текст описания поста будет здесь. Это краткое описание содержания поста, которое дает пользователям представление о том, что их ждет внутри.</p>

            <div className={S.post_image_content}>[Изображение поста]</div>

            <div className={S.post_stats}>
                <span>❤️ 0</span>
                <span>💬 0</span>
                <span>🔁 0</span>
                <span>👁️ 0</span>
            </div>
        </div>
    </div>
  )
}

export default Post