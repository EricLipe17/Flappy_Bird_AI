/*
 * Copyright (C) 2008-2015 by Holger Arndt
 *
 * This file is part of the Universal Java Matrix Package (UJMP).
 * See the NOTICE file distributed with this work for additional
 * information regarding copyright ownership and licensing.
 *
 * UJMP is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * UJMP is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with UJMP; if not, write to the
 * Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
 * Boston, MA  02110-1301  USA
 */

package org.ujmp.core.util.concurrent;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public abstract class BackgroundTask {

	private final Object[] objects;

	private final Future<?> future;

	private final ExecutorService es = Executors.newSingleThreadExecutor();

	public BackgroundTask(final Object... objects) {
		this.objects = objects;
		future = es.submit(new BackgroundTaskCallable());
	}

	public abstract Object run();

	public Object getResult() throws InterruptedException, ExecutionException {
		Object result = future.get();
		es.shutdown();
		return result;
	}

	public final Object getObject(final int i) {
		return objects[i];
	}

	class BackgroundTaskCallable implements Callable<Object> {

		public BackgroundTaskCallable() {
		}

		public final Void call() throws Exception {
			try {
				run();
			} catch (Exception e) {
				e.printStackTrace();
			}
			return null;
		}

	}

}
