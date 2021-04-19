import React, { Component } from 'react';

class Contact extends Component {
    render() {
        return (
            <div>
                <div className="page">
                    <nav id="colorlib-main-nav" role="navigation">
                        <a className="js-colorlib-nav-toggle colorlib-nav-toggle active"><i></i></a>
                        <div className="js-fullheight colorlib-table">
                            <div className="img" style={{ backgroundImage: 'url(/assets/images/img-2.jfif)' }}></div>
                            <div className="colorlib-table-cell js-fullheight">
                                <div className="row no-gutters">
                                    <div className="col-md-12 text-center">
                                        <h1 className="mb-4"><a href="index.html" className="logo">Star In Making<br /><span>Casting Agency</span></a></h1>
                                        <ul>
                                            <li><a href="/"><span>Home</span></a></li>
                                            <li><a href="/about"><span>About</span></a></li>
                                            <li><a href="/actors"><span>Actors</span></a></li>
                                            <li><a href="/movies"><span>Movies</span></a></li>
                                            <li className="active"><a href="/contact"><span>Contact</span></a></li>
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
                                    <a className="colorlib-logo" href="index.html">Star In aking<br /><span>Casting Agency</span></a>
                                </div>
                                <a className="js-colorlib-nav-toggle colorlib-nav-toggle"><i></i></a>
                            </div>
                        </header>

                        <section className="hero-wrap" style={{ backgroundImage: 'url(assets/images/img-5.jpg)' }}>
                            <div className="overlay"></div>
                            <div className="container">
                                <div className="row no-gutters text align-items-end justify-content-center" data-scrollax-parent="true">
                                    <div className="col-md-8 ftco-animate text-center">
                                        <p className="breadcrumbs"><span className="mr-2"><a href="index.html">Home</a></span> <span>Contact</span></p>
                                        <h1 className="mb-5 bread">Contact Us</h1>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <section className="ftco-section contact-section">
                            <div className="container mt-5">
                                <div className="row block-9">
                                    <div className="col-md-4 order-last contact-info ftco-animate">
                                        <div className="row">
                                            <div className="col-md-12 mb-4">
                                                <h2>Contact Information</h2>
                                            </div>
                                            <div className="col-md-12 mb-3">
                                                <p><span>Address:</span> VL Mehta Road, Juhu, Mumbai – 400049, Maharashtra, India</p>
                                            </div>
                                            <div className="col-md-12 mb-3">
                                                <p><span>Phone:</span> <a href="tel://1234567920">+91 1234 987654</a></p>
                                                <p><span>Mobile:</span><a href="tel://1234567920">+91 9987 554447</a></p>
                                            </div>
                                            <div className="col-md-12 mb-3">
                                                <p><span>Email:</span> <a href="mailto:info@yoursite.com">info@starinmaking.com</a></p>
                                            </div>
                                            <div className="col-md-12 mb-3">
                                                <p><span>Website:</span> <a href="www.starinmaking.com">www.starinmaking.com</a></p>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-1"></div>
                                    <div className="col-md-6 order-first ftco-animate">
                                        <form action="#">
                                            <div className="form-group">
                                                <input type="text" className="form-control" placeholder="Your Name" />
                                            </div>
                                            <div className="form-group">
                                                <input type="text" className="form-control" placeholder="Your Email" />
                                            </div>
                                            <div className="form-group">
                                                <input type="text" className="form-control" placeholder="Subject" />
                                            </div>
                                            <div className="form-group">
                                                <textarea name="" id="" cols="30" rows="7" className="form-control" placeholder="Message"></textarea>
                                            </div>
                                            <div className="form-group">
                                                <input type="submit" value="Send Message" className="btn btn-primary py-3 px-5" />
                                            </div>
                                        </form>
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
                                                    <li><a><span className="icon icon-phone"></span><span className="text">+91 1234 987654</span></a></li>
                                                    <li><a><span className="icon icon-envelope"></span><span className="text">info@starinmaking.com</span></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12 text-center">

                                        <p>Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved</p>
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


export default Contact;