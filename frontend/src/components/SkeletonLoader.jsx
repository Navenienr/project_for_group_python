import React from 'react'
import S from '../style/SkeletonLoader.module.css'

const SkeletonLoader = ({ type = 'card', count = 1 }) => {
    const items = Array(count).fill(0);

if (type === 'details') {
    return (
        <div className={S.details_skeleton_wrapper}>
            <div className={S.card_container_skeleton}>

                <div className={S.game_img_skeleton}>
                    <div className={S.game_heading_skeleton}>
                        <div className={S.shimmer_box} style={{ width: '65px', height: '65px', borderRadius: '8px' }}></div>
                        <div className={S.shimmer_box} style={{ width: '250px', height: '30px', marginLeft: '20px', borderRadius: '6px' }}></div>
                    </div>

                    <div className={S.shimmer_box} style={{ width: '100%', height: '500px', borderRadius: '10px' }}></div>
                    <div className={S.thumbs_skeleton}>
                        {Array(5).fill(0).map((_, i) => (
                            <div key={i} className={S.shimmer_box} style={{ width: '172px', height: '95px', borderRadius: '6px' }}></div>
                        ))}
                    </div>
                </div>
                <div className={S.game_info_wrapper_skeleton}>
                    <div className={S.game_info_skeleton_box}>
                        <div className={S.shimmer_box} style={{ width: '100%', height: '250px', opacity: 0.4 }}></div>
                        <div className={S.actions_skeleton}>
                            <div className={S.shimmer_box} style={{ width: '100%', height: '55px', borderRadius: '8px' }}></div>
                            <div className={S.shimmer_box} style={{ width: '100%', height: '50px', borderRadius: '8px', opacity: 0.5 }}></div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    );
}
    const content = items.map((_, index) => (
        <div key={index} className={type === 'card' ? S.card_item : S.list_item}>
            <div className={S.shimmer_box}></div>
            {type === 'card' && <div className={S.card_title_line}></div>}
            {type === 'list' && (
                <div className={S.text_group}>
                    <div className={S.title_line}></div>
                    <div className={S.subtitle_line}></div>
                </div>
            )}
        </div>
    ));

    if (type === 'card') return <>{content}</>;
    return <div className={S.list_wrapper}>{content}</div>;
};

export default SkeletonLoader
