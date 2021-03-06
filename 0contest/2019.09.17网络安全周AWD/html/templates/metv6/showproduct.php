<?php defined('IN_MET') or exit('No permission'); ?>
<include file="head.php" />
<main class="met-showproduct pagetype1 animsition" m-id="noset">
    <div class="met-showproduct-head page-content block-bg">
        <div class="container">
            <div class="row">
                <div class="col-lg-7">
                    <list data="$data['displayimgs']" name="$s"></list>
                    <div class='met-showproduct-list fngallery cover text-xs-center<if value="$s['sub'] gt 1">slick-dotted</if>' id='met-imgs-slick' m-id='noset' m-type='displayimgs'>
                        <!--fngallery：启用lightGallery插件的类名-->
                        <list data="$data['displayimgs']" name="$s">
                        <div class='slick-slide'>
                            <a href='{$s.img}' data-size='{$s.x}x{$s.y}' data-med='{$s.img}' data-med-size='{$s.x}x{$s.y}' class='lg-item-box' data-src='{$s.img}' data-exthumbimage="{$s.img|thumb:60,60}" data-sub-html='{$s.title}'>
                                <!--类名lg-item-box之前为initPhotoSwipeFromDOM插件所用参数；之后为lightGallery插件所用参数，lg-item-box：lightGallery插件对应的类名-->
                                <img
                                <if value="$s['sub'] gt 1">data-lazy<else/>src</if>
                                ="{$s.img|thumb:$c['met_productdetail_x'],$c['met_productdetail_y']}" class='img-fluid' alt='{$s.title}' />
                            </a>
                        </div>

                        </list>
                    </div>
                </div>
                <div class="col-lg-5">
                    <div class="product-intro">
                        <h1 class='m-t-0 font-size-24'>{$data.title}</h1>
                        <if value="$data['description']">
                        <p class='description'>{$data.description}</p>
                        </if>
                        <ul class="product-para paralist blocks-100 blocks-sm-2 blocks-md-3 blocks-lg-2">
                            <list data="$data['para']" name="$s">
                            <li>
                                <span>{$s.name}：</span>
                                {$s.value}
                            </li>
                            </list>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="met-showproduct-body page-content">
        <div class="container">
            <div class="row">
                <div class="col-lg-9 pull-lg-right">
                    <div class="row">
                        <div class="panel panel-body m-b-0 product-detail" boxmh-mh>
                            <ul class="nav nav-tabs nav-tabs-line m-b-20 met-showproduct-navtabs">
                                <list data="$data['contents']" name="$s">
                                <li class="nav-item">
                                    <a
                                    class='nav-link
                                    <if value="$s['_first']">
                                    active
                                    </if>
                                    ' data-toggle="tab" href="#product-content{$s._index}" data-get="product-details">{$s.title}</a>
                                </li>
                                </list>
                            </ul>
                            <article class="tab-content">
                                <list data="$data['contents']" name="$s">
                                <section class="tab-pane met-editor clearfix animation-fade
                                    <if value="$s['_first']">
                                    active
                                    </if>
                                    " id="product-content{$s._index}">
                                    {$s.content}
                                </section>
                                </list>
                            </article>
                            <div class="detail_tag font-size-14">
                                <span>{$data.tagname}</span>
                                <list data="$data[taglist]" name="$tag">
                                    <a href="{$tag.url}" title="{$tag.name}">{$tag.name}</a>
                                </list>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3">
                    <div class="row">
                        <aside class="panel panel-body m-b-0 product-hot met-sidebar leftsidebar" boxmh-h m-id='product_bar'>
                            <div class='sidebar-piclist'>
                                <h3 class='m-0 font-size-16 font-weight-300'>{$lang.product_sidebar_piclist_title}</h3>
                                <ul class='blocks-2 blocks-md-3 blocks-lg-100 m-t-20 text-xs-center imagesize sidebar-piclist-ul' data-scale='{$v.img_x}x{$v.img_y}'>
                                    <tag action='list' cid="$data['class1']" num="$lang['product_sidebar_piclist_num']" type="$lang['product_sidebar_piclist_type']">
                                    <li class='masonry-child'>
                                        <a href='{$v.url}' title='{$v.title}' class='block m-b-0' target='_blank'>
                                            <img data-original="{$v.imgurl|thumb:$v['img_x'],$v['img_y']}" class='cover-image' alt='{$v.title}' height='100'></a>
                                        <h4 class='m-t-10 m-b-0 font-size-14'>
                                            <a href='{$v.url}' title='{$v.title}' target='_blank'>{$v.title}</a>
                                        </h4>
                                    </li>
                                    </tag>
                                </ul>
                            </div>
                        </aside>
                    </div>
                </div>
            </div>
        </div>
    </div>
</main>
<include file="foot.php" />