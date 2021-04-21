import React, { Component } from 'react';


class Home extends Component {
    render() {
        return (
            <div>
                <div className="page">
                    <nav id="colorlib-main-nav" role="navigation">
                        <a className="js-colorlib-nav-toggle colorlib-nav-toggle active"><i></i></a>
                        <div className="js-fullheight colorlib-table">
                            <div className="img" style={{ backgroundImage: 'url(assets/images/img-2.jfif)' }}></div>
                            <div className="colorlib-table-cell js-fullheight">
                                <div className="row no-gutters">
                                    <div className="col-md-12 text-center">
                                        <h1 className="mb-4"><a href="index.html" className="logo">Star in Making<br /><span>Casting Agency</span></a></h1>
                                        <ul>
                                        <li className="active"><a href="/"><span>Home</span></a></li>
                                        <li><a href="/about"><span>About</span></a></li>
                                        <li><a href="/actors"><span>Actors</span></a></li>
                                        <li><a href="/movies"><span>Movies</span></a></li>
                                        <li><a href="/contact"><span>Contact</span></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </nav>
                    <div id="colorlib-page">
                        <header>
                            <div className="container">
                                <div className="colorlib-navbar-brand">
                                    <a className="colorlib-logo" href="index.html">Star in Making<br /><span>Casting Agency</span></a>
                                </div>
                                <a href="#" className="js-colorlib-nav-toggle colorlib-nav-toggle"><i></i></a>
                            </div>
                        </header>

                        <section id="home" className="video-hero js-fullheight" style={{ height: '700px', backgroundImage: 'url(assets/images/bg_1.jpg)', backgroundSize: 'cover', backgroundPosition: 'center center', backgroundAttachment: 'fixed' }}>
                            <div className="overlay"></div>
                            <a className="player" data-property="{videoURL:'https://www.youtube.com/watch?v=onzY9GFhxfg',containment:'#home', showControls:false, autoPlay:true, loop:true, mute:true, startAt:0, opacity:1, quality:'default'}"></a>
                            <div className="container">
                                <div className="row js-fullheight justify-content-center d-flex align-items-center">
                                    <div className="col-md-8">
                                        <div className="text text-center">
                                            <span className="subheading">Welcome to</span>
                                            <h2>Star in Making</h2>
                                            <h3 className="mb-4">A Professional Casting Agency</h3>
                                            <p><a href="/contact" className="btn btn-primary py-3 px-4">Become A Actor</a></p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <section className="ftco-section ftco-no-pt ftco-featured-model">
                            <div className="container-fluid">
                                <div className="row">
                                    <div className="col-md-6 col-lg-3">
                                        <div className="model-entry">
                                            <div className="model-img" style={{ backgroundImage: 'url(assets/images/image_10.jpg)' }}>
                                                <div className="name text-center">
                                                    <h3><a href="#">Anny</a></h3>
                                                </div>
                                                <div className="text text-center">
                                                    <h3><a href="model-single.html">Anny<br /><span>Smitha</span></a></h3>
                                                    <div className="d-flex models-info">
                                                        <div className="box">
                                                            <p>Age</p>
                                                            <span>22</span>
                                                        </div>
                                                        <div className="box">
                                                            <p>Gender</p>
                                                            <span>Female</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <div className="col-md-6 col-lg-3">
                                        <div className="model-entry">
                                            <div className="model-img" style={{ backgroundImage: 'url(assets/images/image_2.jpg)' }}>
                                                <div className="name text-center">
                                                    <h3><a href="#">Priyanka</a></h3>
                                                </div>
                                                <div className="text text-center">
                                                    <h3><a href="#">Priyanka<br /><span>Chopra Jonas</span></a></h3>
                                                    <div className="d-flex models-info">
                                                        <div className="box">
                                                            <p>Age</p>
                                                            <span>38</span>
                                                        </div>
                                                        <div className="box">
                                                            <p>Gender</p>
                                                            <span>Female</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <div className="col-md-6 col-lg-3">
                                        <div className="model-entry">
                                            <div className="model-img" style={{ backgroundImage: 'url(assets/images/image_3.jpg)' }}>
                                                <div className="name text-center">
                                                    <h3><a href="model-single.html">Tiger</a></h3>
                                                </div>
                                                <div className="text text-center">
                                                    <h3><a href="#">Tiger<br /><span>Shroff</span></a></h3>
                                                    <div className="d-flex models-info">
                                                        <div className="box">
                                                            <p>Age</p>
                                                            <span>31</span>
                                                        </div>
                                                        <div className="box">
                                                            <p>Gender</p>
                                                            <span>Male</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-6 col-lg-3">
                                        <div className="model-entry">
                                            <div className="model-img" style={{ backgroundImage: 'url(assets/images/image_4.jpg)' }}>
                                                <div className="name text-center">
                                                    <h3><a href="#">Zain</a></h3>
                                                </div>
                                                <div className="text text-center">
                                                    <h3><a href="model-single.html">Zain<br /><span>Imam</span></a></h3>
                                                    <div className="d-flex models-info">
                                                        <div className="box">
                                                            <p>Age</p>
                                                            <span>32</span>
                                                        </div>
                                                        <div className="box">
                                                            <p>Gender</p>
                                                            <span>Male</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>


                        <section className="ftco-section ftco-no-pt ftco-no-pb ftco-about-section">
                            <div className="container-fluid px-0">
                                <div className="row d-md-flex text-wrapper">
                                    <div className="one-half img" style={{ backgroundImage: 'url(assets/images/img-1.jfif)' }}></div>
                                    <div className="one-half half-text d-flex justify-content-end align-items-center">
                                        <div className="text-inner pl-md-5">
                                            <span className="subheading">Hello!</span>
                                            <h3 className="heading">Star In Making</h3>
                                            <h2 className="heading">A Professional Casting Agency</h2>
                                            <p></p>
                                            <p>Star in Making <strong>is India’s First Digital Casting Agency</strong> that consists of Actors and Movies across India. We connect with aspiring Actors and Models, and help them connect with Casting Directors all over the Industry.</p>
                                            <p>We don't take any Commission from our Actors & Models on board.We bring together a whole team of photographers, studios, make-up artists, talent managers, production house tie-ups under one roof.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <section className="ftco-section bg-dark">
                            <div className="container">
                                <div className="row">
                                    <div className="col-md-3">
                                        <div className="services ftco-animate text-center">
                                            <div className="icon d-flex justify-content-center align-items-center"><span className="flaticon-shopping-bag"></span></div>
                                            <div className="info mt-4">
                                                <h3 className="mb-4">PORTFOLIO MANAGEMENT</h3>
                                                <p>Portfolio management is done by the team of experts that will help you connect with the best modeling and casting agencies in town.</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-3">
                                        <div className="services ftco-animate text-center">
                                            <div className="icon d-flex justify-content-center align-items-center"><span className="flaticon-photo-camera"></span></div>
                                            <div className="info mt-4">
                                                <h3 className="mb-4">PHOTOGRAPHERS</h3>
                                                <p>The best fashion photographers are on board. Your photographs are the first impression of you, so let it be the best. We trust in the best.</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-3">
                                        <div className="services ftco-animate text-center">
                                            <div className="icon d-flex justify-content-center align-items-center"><span className="flaticon-quality"></span></div>
                                            <div className="info mt-4">
                                                <h3 className="mb-4">STUDIO & MAKE-UP</h3>
                                                <p>We provide studios for all kinds of photo shoots. Whenever make-up is needed, we have the best make-up artists at your service.</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-3">
                                        <div className="services ftco-animate text-center">
                                            <div className="icon d-flex justify-content-center align-items-center"><span className="flaticon-megaphone"></span></div>
                                            <div className="info mt-4">
                                                <h3 className="mb-4">MEDIA HOUSES</h3>
                                                <p>We have a team set up for media house tie-ups. We love to ensure auditions and jobs for all those listed on our platform.</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <section className="ftco-section ftco-no-pt ftco-no-pb">
                            <div className="container-fluid px-4">
                                <div className="row d-flex">
                                    <div className="col-md-6 col-lg-3 d-flex align-items-center ftco-animate">
                                        <div className="heading-section text-center">
                                            <h2 className="">Our Tops Actor's</h2>
                                            <p>are handpicked and boast a varied range of talent.</p>
                                        </div>
                                    </div>
                                    <div className="col-md-6 col-lg-3 ftco-animate">
                                        <div className="model-entry">
                                            <div className="model-img" style={{ backgroundImage: 'url(assets/images/image_10.jpg)' }}>
                                                <div className="name text-center">
                                                    <h3><a href="#">Anny</a></h3>
                                                </div>
                                                <div className="text text-center">
                                                    <h3><a href="#">Anny<br /><span>Smitha</span></a></h3>
                                                    <div className="d-flex models-info">
                                                        <div className="box">
                                                            <p>Age</p>
                                                            <span>22</span>
                                                        </div>
                                                        <div className="box">
                                                            <p>Gender</p>
                                                            <span>Female</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-6 col-lg-3 ftco-animate">
                                        <div className="model-entry">
                                            <div className="model-img" style={{ backgroundImage: 'url(assets/images/image_2.jpg)' }}>
                                                <div className="name text-center">
                                                    <h3><a href="#">Priyanka</a></h3>
                                                </div>
                                                <div className="text text-center">
                                                    <h3><a href="#">Priyanka<br /><span>Chopra Jonas</span></a></h3>
                                                    <div className="d-flex models-info">
                                                        <div className="box">
                                                            <p>Age</p>
                                                            <span>38</span>
                                                        </div>
                                                        <div className="box">
                                                            <p>Gender</p>
                                                            <span>Female</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-6 col-lg-3 d-flex justify-content-center align-items-center ftco-animate">
                                        <div className="btn-view">
                                            <p><a href="/actors" className="btn btn-white py-3 px-5">View more</a></p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <section className="ftco-section">
                            <div className="container">
                                <div className="row justify-content-center">
                                    <div className="col-md-8 mb-5 heading-section text-center ftco-animate">
                                        <span className="subheading">Movies</span>
                                        <h2 className="mb-4">Recent Movies</h2>
                                    </div>
                                </div>
                                <div className="row d-flex">
                                    <div className="col-md-4 d-flex ftco-animate">
                                        <div className="blog-entry bg-dark align-self-stretch">
                                            <a href="#" className="block-20" style={{ backgroundImage: 'url(assets/images/mv-1.jpg)' }}>
                                            </a>
                                            <div className="text p-4 d-block">
                                                <div className="meta mb-3">
                                                </div>
                                                <h3 className="heading mt-3"><a href="#">The Girl on the Train</a></h3>
                                                <p>Release Date: 26 Feb 2021</p>
                                                <p><a href="https://in.bookmyshow.com" className="btn btn-primary">Book Tickets</a></p>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-4 d-flex ftco-animate">
                                        <div className="blog-entry bg-dark align-self-stretch">
                                            <a href="blog-single.html" className="block-20" style={{ backgroundImage: 'url(assets/images/mv-2.jpg)' }}>
                                            </a>
                                            <div className="text p-4 d-block">
                                                <div className="meta mb-3">
                                                </div>
                                                <h3 className="heading mt-3"><a href="#">Godzilla vs. Kong</a></h3>
                                                <p>Release Date: 26 March 2021</p>
                                                <p><a href="https://in.bookmyshow.com" className="btn btn-primary">Book Tickets</a></p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <section className="ftco-section testimony-section img" style={{ backgroundImage: 'url(assets/images/bg_2.jpg)' }}>
                            <div className="overlay"></div>
                            <div className="container">
                                <div className="row d-md-flex justify-content-center">
                                    <div className="col-md-8 ftco-animate">
                                        <div className="carousel-testimony owl-carousel">
                                            <div className="item">
                                                <div className="testimony-wrap text-center">
                                                    <div className="user-img mb-5" style={{ backgroundImage: 'url(assets/images/pic-1.jpg)' }}>
                                                        <span className="quote d-flex align-items-center justify-content-center">
                                                            <i className="icon-quote-left"></i>
                                                        </span>
                                                    </div>
                                                    <div className="text">
                                                        <p className="mb-5">It was a great experience with Star In Making Team.The team members are nice and supportive.I got a big break.Thank you for this big oppertunity.</p>
                                                        <p className="name">Myra</p>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="item">
                                                <div className="testimony-wrap text-center">
                                                    <div className="user-img mb-5" style={{ backgroundImage: 'url(assets/images/pic-2.jpg)' }}>
                                                        <span className="quote d-flex align-items-center justify-content-center">
                                                            <i className="icon-quote-left"></i>
                                                        </span>
                                                    </div>
                                                    <div className="text">
                                                        <p className="mb-5">I am so glad to be associated with Star In Making.I am going to be casted upcoming bollywood movie.Thank you so much Star In Making.</p>
                                                        <p className="name">Arnav</p>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="item">
                                                <div className="testimony-wrap text-center">
                                                    <div className="user-img mb-5" style={{ backgroundImage: 'url(assets/images/pic-3.webp)' }}>
                                                        <span className="quote d-flex align-items-center justify-content-center">
                                                            <i className="icon-quote-left"></i>
                                                        </span>
                                                    </div>
                                                    <div className="text">
                                                        <p className="mb-5">Great team,professionalism upto the mark.I shot for pinwheel project.Thanks Star in Making.It's a dream comes true.</p>
                                                        <p className="name">Karishma</p>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="item">
                                                <div className="testimony-wrap text-center">
                                                    <div className="user-img mb-5" style={{ backgroundImage: 'url(assets/images/pic-4.jpg)' }}>
                                                        <span className="quote d-flex align-items-center justify-content-center">
                                                            <i className="icon-quote-left"></i>
                                                        </span>
                                                    </div>
                                                    <div className="text">
                                                        <p className="mb-5">I was great learning experience.The whole Star In Making team quit supportive throughout shooting.Lovly working with Star In Making.</p>
                                                        <p className="name">Raghav</p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <section className="ftco-appointment ftco-section">
                            <div className="overlay"></div>
                            <div className="container">
                                <div className="row justify-content-center">
                                    <div className="col-md-8 mb-5 heading-section text-center ftco-animate">
                                        <span className="subheading">Star In Making</span>
                                        <h2 className="mb-4">Contact Us</h2>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-4">
                                        <div className="row">
                                            <div className="col-md-12 mb-3">
                                                <p><span>Address:</span> VL Mehta Road, Juhu, Mumbai – 400049, Maharashtra, India</p>
                                            </div>
                                            <div className="col-md-12 mb-3">
                                                <p><span>Phone:</span> <a href="tel://1234567920">+91 1234 987654</a></p>
                                            </div>
                                            <div className="col-md-12 mb-3">
                                                <p><span>Email:</span> <a href="mailto:info@yoursite.com">info@starinmaking.com</a></p>
                                            </div>
                                            <div className="col-md-12 mb-3">
                                                <p><span>Website:</span> <a href="#">starinmaking.com</a></p>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-8 appointment ftco-animate">
                                        <form action="#" className="appointment-form">
                                            <div className="row">
                                                <div className="col-md-6">
                                                    <div className="d-md-flex">
                                                        <div className="form-group">
                                                            <input type="text" className="form-control" placeholder="First Name" />
                                                        </div>
                                                    </div>
                                                </div>
                                                <div className="col-md-6">
                                                    <div className="d-me-flex">
                                                        <div className="form-group">
                                                            <input type="text" className="form-control" placeholder="Last Name" />
                                                        </div>
                                                    </div>
                                                </div>
                                                <div className="col-md-6">
                                                    <div className="d-me-flex">
                                                        <div className="form-group">
                                                            <input type="text" className="form-control" placeholder="Email Address" />
                                                        </div>
                                                    </div>
                                                </div>
                                                <div className="col-md-6">
                                                    <div className="d-me-flex">
                                                        <div className="form-group">
                                                            <input type="text" className="form-control" placeholder="Your City" />
                                                        </div>
                                                    </div>
                                                </div>
                                                <div className="col-md-12">
                                                    <div className="form-group">
                                                        <textarea name="" id="" cols="30" rows="10" className="form-control" placeholder="Message"></textarea>
                                                    </div>
                                                </div>
                                                <div className="col-md-12">
                                                    <div className="form-group">
                                                        <input type="submit" value="Send A Message" className="btn btn-primary py-3 px-4" />
                                                    </div>
                                                </div>

                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </section>


                        <section className="ftco-quote ftco-section ftco-animate">
                            <div className="container">
                                <div className="row d-flex">
                                    <div className="col-md-6 req-quote py-5 text-center align-items-center img" style={{ backgroundImage: 'url(assets/images/bg_2.jpg)' }}>
                                        <h3 className="ml-md-3">Become An Actor?</h3>
                                        <span className="ml-md-3"><a href="/contact">Call us now to know how!</a></span>
                                    </div>
                                    <div className="col-md-6 req-quote py-5 text-center align-items-center img" style={{ backgroundImage: 'url(assets/images/img-4.jfif)' }}>
                                        <h3 className="ml-md-3">UpComing Movies</h3>
                                        <span className="ml-md-3"><a href="/movies">Know more</a></span>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <footer className="ftco-footer ftco-section img">
                            <div className="overlay"></div>
                            <div className="container">
                                <div className="row mb-5">
                                    <div className="col-md-3">
                                        <div className="ftco-footer-widget mb-4">
                                            <h2 className="ftco-heading-2 logo"><a href="index.html">Star In Making</a></h2>
                                            <p>Becoming a celebrity is now a one step away. Build a portfolio & let it speak for you.</p>
                                            <ul className="ftco-footer-social list-unstyled float-md-left float-lft mt-5">
                                                <li className="ftco-animate"><a href="#"><span className="icon-twitter"></span></a></li>
                                                <li className="ftco-animate"><a href="#"><span className="icon-facebook"></span></a></li>
                                                <li className="ftco-animate"><a href="#"><span className="icon-instagram"></span></a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div className="col-md-4">
                                    </div>
                                    <div className="col-md-2">
                                        <div className="ftco-footer-widget mb-4 ml-md-4">
                                            <h2 className="ftco-heading-2">Site Links</h2>
                                            <ul className="list-unstyled">
                                                <li><a href="/" className="py-2 d-block">Home</a></li>
                                                <li><a href="/about" className="py-2 d-block">About</a></li>
                                                <li><a href="/actors" className="py-2 d-block">Actors</a></li>
                                                <li><a href="/movies" className="py-2 d-block">Movies</a></li>
                                                <li><a href="/about" className="py-2 d-block">Services</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div className="col-md-3">
                                        <div className="ftco-footer-widget mb-4">
                                            <h2 className="ftco-heading-2">Reach Us</h2>
                                            <div className="block-23 mb-3">
                                                <ul>
                                                    <li><span className="icon icon-map-marker"></span><span className="text">VL Mehta Road, Juhu, Mumbai – 400049, Maharashtra, India</span></li>
                                                    <li><a href="#"><span className="icon icon-phone"></span><span className="text">+91 1234 987654</span></a></li>
                                                    <li><a href="#"><span className="icon icon-envelope"></span><span className="text">info@starinmaking.com</span></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12 text-center">

                                        <p>Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved.</p>
                                    </div>
                                </div>
                            </div>
                        </footer>



                    </div>
                </div>
            </div>
        )
    }
}


export default Home;